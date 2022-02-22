import frappe

def lead_query(user = frappe.session.user):
    pass
    if ('CRM User' in frappe.get_roles(user) and not 'Sales Manager' in frappe.get_roles(user)):
        print('\n\n\n<<<<<<<<<<<<Inside Lead MAPPING QUERY>>>>>>>>>>>>\n\n\n')
        return "(`tabLead`.telecaller_name = '{user}')".format(user=frappe.session.user)
    if ('Sales User' in frappe.get_roles(user) and not 'Sales Manager' in frappe.get_roles(user)):
        print('\n\n\n<<<<<<<<<<<<Inside Lead MAPPING QUERY>>>>>>>>>>>>\n\n\n')
        return "(`tabLead`.lead_owner = '{user}')".format(user=frappe.session.user)
    



