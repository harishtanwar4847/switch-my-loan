import frappe

def execute():
    try:
        frappe.get_doc({'doctype': 'Role', 'role_name': 'CRM User'}).insert()
    except frappe.DuplicateEntryError:
        pass