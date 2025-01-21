# Copyright (c) 2025, ahmed atef and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from send_email_integration.utils.helper_functions import get_sending_api_key_and_signning_secret
import resend



class SendEmailRecord(Document):
	@frappe.whitelist()
	def on_submit(self):
		self.send_email_to_all_users()

	def send_email_to_all_users(self):
		api_key = get_sending_api_key_and_signning_secret().get('api_key')
		resend.api_key = api_key if api_key else frappe.throw("Please Check Api Key!")
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
		self.reload()


