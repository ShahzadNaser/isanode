import frappe

def after_install():
	frappe.db.set_value('System Settings', None, 'app_name', 'Application')