import frappe
from frappe.core.doctype.data_import.data_import import import_file

def execute():
    path = frappe.get_app_path('switch_my_loan','patches','product2.csv')
    import_file('Product', path, 'Insert',console=True)