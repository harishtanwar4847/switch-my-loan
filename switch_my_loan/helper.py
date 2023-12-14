import frappe

@frappe.whitelist()
def get_logged_user_data():
    roles = frappe.get_roles(frappe.session.user)
    return {
        "user": frappe.session.user,
        "session": frappe.session.data,
        "roles": roles,
        "name": frappe.session.data.full_name
    }

@frappe.whitelist()
def create_lead():
    doc = frappe.new_doc('Lead')
    lead_data = frappe.form_dict;

    for field, value in lead_data.items():
        if hasattr(doc, field):
            setattr(doc, field, value)

    doc.loan_amount = int(lead_data.get('loan_amount'))

    doc.insert()
    frappe.db.commit()