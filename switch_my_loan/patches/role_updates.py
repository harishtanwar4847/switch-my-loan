from __future__ import unicode_literals
import frappe

def execute():
    doc = frappe.get_doc('Role', 'CRM User')
    doc.form_sidebar = 1
    doc.timeline = 1
    doc.dashboard = 1
    doc.save()
    frappe.db.commit()

    doc2 = frappe.get_doc('Role', 'Sales User')
    doc2.form_sidebar = 1
    doc2.timeline = 1
    doc2.dashboard = 1
    doc2.save()
    frappe.db.commit()

    doc3 = frappe.get_doc('Role', 'Sales Manager')
    doc3.form_sidebar = 1
    doc3.timeline = 1
    doc3.dashboard = 1
    doc3.save()
    frappe.db.commit()

    doc4 = frappe.get_doc('Role', 'CRM Manager')
    doc4.form_sidebar = 1
    doc4.timeline = 1
    doc4.dashboard = 1
    doc4.save()
    frappe.db.commit()

