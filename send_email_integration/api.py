
import frappe
from send_email_integration.utils.constants import EMAIL_STATUS_UPDATE_EVENTS
from send_email_integration.utils.helper_functions import get_sending_api_key_and_signning_secret
from svix.webhooks import Webhook , WebhookVerificationError


@frappe.whitelist(allow_guest = True)
def handle_resend_webhook():
    verify_signning_secret()
    data = frappe.form_dict
    entity , event = data.type.split('.')
    if entity == "email" and event in EMAIL_STATUS_UPDATE_EVENTS:
        send_id = data.data.get("email_id")
        email_status = " ".join(event.split("_")).title()
        frappe.db.set_value("Send Email Record",{'sending_id':send_id},"status",email_status)
    return email_status

@frappe.whitelist()
def send_emails(subject="",from_email="",to_emails=[],email_html="",reply_to="",broadcast=None):
    if isinstance(to_emails,str):
        to_emails = to_emails.strip().split(",")
    for index ,to_email in enumerate(to_emails):
        resend_email_doc = frappe.new_doc("Send Email Record")
        resend_email_doc.from_email = from_email
        resend_email_doc.to_emails = to_email
        resend_email_doc.subject = subject
        resend_email_doc.email_html = email_html
        resend_email_doc.reply_to = reply_to
        resend_email_doc.broadcast = broadcast
        resend_email_doc.save()
        resend_email_doc.submit()
        frappe.publish_progress(round(((index + 1)/len(to_emails)*100)),title="Sending Emails...",description = f"""{index+1} of {len(to_emails)} Sent Successfully""")
    return True


def verify_signning_secret():
    payload = frappe.local.request.data
    headers = frappe.local.request.headers
    secret = get_sending_api_key_and_signning_secret().get('signning_secret')
    try:
        wh = Webhook(secret)
        wh.verify(payload,headers)
    except WebhookVerificationError as e:
        frappe.throw("Webhook Verficiation Error Failed")