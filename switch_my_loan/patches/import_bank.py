import frappe
from frappe.core.doctype.data_import.data_import import import_file

def execute():
    path = frappe.get_app_path('switch_my_loan','patches','bank.csv')
    import_file('Bank', path, 'Insert',console=True)