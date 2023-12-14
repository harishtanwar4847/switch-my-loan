from __future__ import unicode_literals
import frappe

def execute():
    doc = frappe.get_doc('System Settings')
    doc.apply_strict_user_permissions = 1
    doc.allow_login_using_mobile_number = 1
    doc.allow_login_using_user_name = 1
    doc.save()
    frappe.db.commit()