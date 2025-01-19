# Copyright (c) 2025, ahmed atef and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.password import get_decrypted_password
import resend

def get_sending_api_key():
	return get_decrypted_password("Sending Settings","Sending Settings","api_key")

class SendEmailRecord(Document):
	@frappe.whitelist()
	def send(self):
		resend.api_key = get_sending_api_key()
		email = resend.Emails.send({
			"from":self.from_email,
			"to":self.to_emails.strip().split(","),
			"subject":self.subject,
			"html":self.email_html
		})
		self.status = "Sent"
		self.sending_id = email["id"]
		self.save()

