from __future__ import unicode_literals
import frappe

def execute():
    doc = frappe.get_doc('Navbar Settings')
    doc.logo_width = 75
    doc.save()
    frappe.db.commit()