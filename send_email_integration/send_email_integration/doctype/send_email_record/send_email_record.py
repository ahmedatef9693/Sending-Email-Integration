# Copyright (c) 2025, ahmed atef and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from send_email_integration.utils.helper_functions import get_sending_api_key
import resend



class SendEmailRecord(Document):
	@frappe.whitelist()
	def on_submit(self):
		self.send_email_to_all_users()

	def send_email_to_all_users(self):
		resend.api_key = get_sending_api_key()
		email = resend.Emails.send({
			"from":self.from_email,
			"to":self.to_emails.strip().split(","),
			"subject":self.subject,
			"html":self.email_html
		})
		frappe.db.set_value("Send Email Record",self.name,{
			'status':'Sent',
			'sending_id':email["id"]
		})


