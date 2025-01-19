
import frappe

EMAIL_STATUS_UPDATE_EVENTS = [
    "sent",
    "delivered",
    "delivery_delayed",
    "complained",
    "bounced",
    "opened"
    ]


@frappe.whitelist(allow_guest = True)
def handle_resend_webhook():
    data = frappe.form_dict
    
    entity , event = data.type.split('.')
    if entity == "email" and event in EMAIL_STATUS_UPDATE_EVENTS:
        send_id = data.data.get("email_id")
        email_status = " ".join(event.split("_")).title()
        frappe.db.set_value("Send Email Record",{'sending_id':send_id},"status",email_status)
    # breakpoint()
    return data