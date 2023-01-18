import frappe

def execute():
    frappe.db.sql("""UPDATE `tabLead` set obligation = 0.00""")
    frappe.db.commit()
