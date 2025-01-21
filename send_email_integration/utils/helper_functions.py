import frappe
from frappe.utils.password import get_decrypted_password


def get_sending_api_key_and_signning_secret():
	return {
		'api_key':get_decrypted_password("Resend Integration Settings","Resend Integration Settings","api_key"),
		'signning_secret':get_decrypted_password("Resend Integration Settings","Resend Integration Settings","signning_secret")
	}