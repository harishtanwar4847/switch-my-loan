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
    # if 'CRM User' in roles or 'Partner User' in roles:
    #     if all([doc.loan_amount, doc.location, doc.product_required]):
    #         # Fetch the appropriate sales person and amount threshold
    #         result = frappe.db.sql("""
    #             SELECT sales_person, amount_threshold 
    #             FROM `tabProduct Sales Team` 
    #             WHERE parent = %s AND location_name = %s
    #             ORDER BY amount_threshold ASC LIMIT 1
    #         """, (doc.product_required, doc.location), as_dict=1)

    #         if not result:
    #             frappe.throw("Appropriate Sales Person or Amount Threshold not found for this Product")

    #         sales_person, max_amount_threshold = result[0]['sales_person'], result[0]['amount_threshold']

    #         if not (1 <= int(doc.loan_amount) <= max_amount_threshold):
    #             frappe.throw("Loan Amount not within the allowed range for this Product")
    #         # Fetch lead count and reporting manager
    #         lead_info = frappe.db.get_value('Sales Person', sales_person, ['leads_count', 'parent_sales_person'], as_dict=1)

    #         if lead_info:
    #             lead_count = int(lead_info['leads_count'])
    #             reporting_manager = lead_info['parent_sales_person']

    #             # Count leads assigned to the sales person
    #             lead_owner_count = frappe.db.count('Lead', filters={
    #                 'workflow_state': ('not in', ['Amount Credited']),  # Changed to a list
    #                 'lead_owner': sales_person
    #             })
    #             # Assign lead owner based on lead count
    #             if lead_owner_count <= lead_count:
    #                 doc.lead_owner = sales_person
    #             else:
    #                 # frappe.msgprint("Lead limit exceeded, assigning to reporting manager")
    #                 doc.lead_owner = reporting_manager

    #             # Fetch and assign mobile number
    #             doc.lead_owner_mobile_no = frappe.db.get_value('User', doc.lead_owner, 'mobile_no')

    #             # for field, value in lead_data.items():
    #             #     if hasattr(doc, field):
    #             #         setattr(doc, field, value)

    #             # Save the document
    #             doc.bypass_validation = True
    #             doc.insert()
    #             frappe.db.commit()