import frappe
from frappe.core.doctype.data_import.data_import import import_file

def execute():
    try:
        frappe.get_doc({
            'doctype': 'Sales Person',
            'sales_person_name': 'Himanshu',
            'sales_person': 'himanshu@switchmyloan.in',
            'parent_sales_person' : 'Sales Team',
            'is_group':1
        }).insert()
        frappe.get_doc({
            'doctype': 'Sales Person',
            'sales_person_name': 'Sachin',
            'sales_person': 'sachin@switchmyloan.in',
            'parent_sales_person' : 'himanshu@switchmyloan.in',
            'is_group':1
        }).insert()
    except frappe.DuplicateEntryError:
            pass    

    frappe.db.commit()
    path = frappe.get_app_path('switch_my_loan','patches','master_imports','parent_sales_person.csv')
    import_file('Sales Person', path, 'Insert',console=True)

    path1 = frappe.get_app_path('switch_my_loan','patches','master_imports','sales_person.csv')
    import_file('Sales Person', path1, 'Insert',console=True)
