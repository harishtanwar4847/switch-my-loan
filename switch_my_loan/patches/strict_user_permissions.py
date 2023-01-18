from __future__ import unicode_literals
import frappe

def execute():
    doc = frappe.get_doc('System Settings')
    doc.apply_strict_user_permissions = 1
    doc.save()
    frappe.db.commit()