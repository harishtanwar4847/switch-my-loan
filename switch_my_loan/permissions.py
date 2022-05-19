import frappe

def lead_query(user = frappe.session.user):
    pass
    if ('CRM User' in frappe.get_roles(user) and not 'Sales Manager' in frappe.get_roles(user) and not 'System Manager' in frappe.get_roles(user)):
        print('\n\n\n<<<<<<<<<<<<Inside Lead MAPPING QUERY>>>>>>>>>>>>\n\n\n')
        return "(`tabLead`.telecaller_name = '{user}')".format(user=frappe.session.user)
    if ('Sales User' in frappe.get_roles(user) and not 'Sales Manager' in frappe.get_roles(user) and not 'System Manager' in frappe.get_roles(user)):
        print('\n\n\n<<<<<<<<<<<<Inside Lead MAPPING QUERY>>>>>>>>>>>>\n\n\n')
        return "(`tabLead`.lead_owner = '{user}')".format(user=frappe.session.user)
    if ('CRM Manager' in frappe.get_roles(user) and not 'Sales Manager' in frappe.get_roles(user) and not 'System Manager' in frappe.get_roles(user)):
        return "(`tabLead`.telecaller_name is not null)"
    if (frappe.session.user == 'himanshu@switchmyloan.in'):
        return "(`tabLead`.docstatus = 0)"
    if ('Sales Manager' in frappe.get_roles(user) and not 'System Manager' in frappe.get_roles(user)):
        return "((`tabLead`.lead_owner in (SELECT `tabLead`.lead_owner FROM `tabLead` INNER JOIN `tabSales Person` ON `tabLead`.lead_owner = `tabSales Person`.parent_sales_person OR `tabLead`.lead_owner = `tabSales Person`.sales_person where `tabSales Person`.parent_sales_person = '{user}')) OR (`tabLead`.lead_owner = '{user}'))".format(user=frappe.session.user)
    
 
    



