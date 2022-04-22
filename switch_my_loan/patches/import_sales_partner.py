import frappe
from frappe.core.doctype.data_import.data_import import import_file

def execute():
    path = frappe.get_app_path('switch_my_loan','patches','master_imports','sales_partner.csv')
    import_file('Sales Partner', path, 'Insert',console=True)