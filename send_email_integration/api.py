
import frappe
from send_email_integration.utils.constants import EMAIL_STATUS_UPDATE_EVENTS



@frappe.whitelist(allow_guest = True)
def handle_resend_webhook():
    data = frappe.form_dict
    entity , event = data.type.split('.')
    if entity == "email" and event in EMAIL_STATUS_UPDATE_EVENTS:
        send_id = data.data.get("email_id")
        email_status = " ".join(event.split("_")).title()
        frappe.db.set_value("Send Email Record",{'sending_id':send_id},"status",email_status)
    return email_status

@frappe.whitelist()
def send_email(subject="",from_email="",to_emails=[],email_html="",reply_to=""):
    if isinstance(to_emails,str):
        to_emails = to_emails.strip().split(",")
    for to_email in to_emails:
        resend_email_doc = frappe.new_doc("Send Email Record")
        resend_email_doc.from_email = from_email
        resend_email_doc.to_emails = to_email
        resend_email_doc.subject = subject
        resend_email_doc.email_html = email_html
        resend_email_doc.reply_to = reply_to
        resend_email_doc.save()
        resend_email_doc.submit()
    return True