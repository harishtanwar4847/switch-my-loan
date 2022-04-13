import frappe
from frappe.core.doctype.data_import.data_import import import_file

def execute():
    try:
        frappe.get_doc({
            'doctype': 'Territory',
            'territory_name': 'Mumbai',
            'parent_territory' : 'All Territories',
            'is_group':1
        }).insert()
    except frappe.DuplicateEntryError:
            pass    

    frappe.db.commit()
    path = frappe.get_app_path('switch_my_loan','patches','master_imports','parent_territory.csv')
    import_file('Territory', path, 'Insert',console=True)

    path1 = frappe.get_app_path('switch_my_loan','patches','master_imports','territory.csv')
    import_file('Territory', path1, 'Insert',console=True)