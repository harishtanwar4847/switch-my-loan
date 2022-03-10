import frappe

def execute():
    try:
        frappe.get_doc({'doctype': 'Role', 'role_name': 'CRM Manager'}).insert()
    except frappe.DuplicateEntryError:
        pass