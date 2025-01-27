# Copyright (c) 2025, ahmed atef and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from send_email_integration.api import send_email

class SendEmailBroadcast(Document):    
	@frappe.whitelist()
	def send_emails(self):
		send_email(
			subject=self.subject,
			from_email=self.from_email,
			to_emails=self.recipients,
			reply_to=self.reply_to,
			broadcast = self.name,
			email_html=self.email_html)
		self.status = "Sent"
		self.save()

