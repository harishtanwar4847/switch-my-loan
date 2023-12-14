from __future__ import unicode_literals
import frappe

def create_role_if_not_exists(role_name):
    if not frappe.db.exists("Role", role_name):
        doc = frappe.new_doc("Role")
        doc.role_name = role_name
        doc.form_sidebar = 1
        doc.timeline = 1
        doc.dashboard = 1
        doc.insert()

def execute():
    role_list = ["Restrict Fields Export"]

    for role in role_list:
        create_role_if_not_exists(role)

    frappe.db.commit()