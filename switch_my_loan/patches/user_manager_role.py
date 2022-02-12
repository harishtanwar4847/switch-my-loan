import frappe

def execute():
    try:
        frappe.get_doc({'doctype': 'Role', 'role_name': 'User Manager'}).insert()
    except frappe.DuplicateEntryError:
        pass