import frappe

def execute():
    try:
        frappe.get_doc({'doctype': 'Role', 'role_name': 'Exco'}).insert()
    except frappe.DuplicateEntryError:
        pass