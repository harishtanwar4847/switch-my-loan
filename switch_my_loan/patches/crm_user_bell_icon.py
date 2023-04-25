import frappe

def execute():
    role = frappe.get_doc("Role", "CRM User")
    role.notifications = 1
    role.save()