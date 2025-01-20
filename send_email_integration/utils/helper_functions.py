import frappe
from frappe.utils.password import get_decrypted_password


def get_sending_api_key():
	return get_decrypted_password("Sending Settings","Sending Settings","api_key")