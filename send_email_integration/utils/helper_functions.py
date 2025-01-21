import frappe
from frappe.utils.password import get_decrypted_password


def get_sending_api_key():
	return get_decrypted_password("Resend Integration Settings","Resend Integration Settings","api_key")