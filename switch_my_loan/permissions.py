import frappe

def lead_query(user = frappe.session.user):
    if (frappe.get_roles(user)):
        print('\n\n\n<<<<<<<<<<<<Inside Lead MAPPING QUERY>>>>>>>>>>>>\n\n\n')
        return "(`tabLead`.telecaller_name = '{user}' or `tabLead`.lead_owner = '{user}')".format(user=frappe.session.user)
    if (frappe.get_roles(user)):
        print('\n\n\n<<<<<<<<<<<<Inside Lead MAPPING QUERY>>>>>>>>>>>>\n\n\n')
        return "(`tabLead`.lead_owner = '{user}')".format(user=frappe.session.user)
    



