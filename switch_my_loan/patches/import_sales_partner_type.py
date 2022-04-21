import frappe
from frappe.core.doctype.data_import.data_import import import_file

def execute():
    path = frappe.get_app_path('switch_my_loan','patches','master_imports','sales_partner_type.csv')
    import_file('Sales Partner Type', path, 'Insert',console=True)