import frappe

def lead_query(user = frappe.session.user):
    pass
    if (('CRM User' in frappe.get_roles(user) or 'Partner User' in frappe.get_roles(user)) and not 'Sales Manager' in frappe.get_roles(user) and not 'System Manager' in frappe.get_roles(user) and not 'Sales User' in frappe.get_roles(user)):
        print('\n\n\n<<<<<<<<<<<<Inside Lead MAPPING QUERY>>>>>>>>>>>>\n\n\n')
        return "(`tabLead`.telecaller_name = '{user}')".format(user=frappe.session.user)
    if ('Sales User' in frappe.get_roles(user) and not 'Sales Manager' in frappe.get_roles(user) and not 'System Manager' in frappe.get_roles(user)):
        print('\n\n\n<<<<<<<<<<<<Inside Lead MAPPING QUERY>>>>>>>>>>>>\n\n\n')
        return "(`tabLead`.lead_owner = '{user}')".format(user=frappe.session.user)
    if (('CRM Manager' in frappe.get_roles(user) or 'Partner Manager' in frappe.get_roles(user)) and not 'Sales Manager' in frappe.get_roles(user) and not 'System Manager' in frappe.get_roles(user)):
        return "(`tabLead`.telecaller_name is not null)"
    if (frappe.session.user == 'himanshu@switchmyloan.in'):
        return "(`tabLead`.docstatus = 0)"
    if ('Sales Manager' in frappe.get_roles(user) and not 'System Manager' in frappe.get_roles(user)):
        
        # return """((`tabLead`.lead_owner in (SELECT `tabLead`.lead_owner FROM `tabLead` INNER JOIN `tabSales Person` ON 
        # `tabLead`.lead_owner = `tabSales Person`.parent_sales_person OR 
        # `tabLead`.lead_owner = `tabSales Person`.sales_person where `tabSales Person`.parent_sales_person = '{user}')) OR 
        # `tabLead`.lead_owner = `tabSales Person`.sales_person where 
        # OR (`tabLead`.lead_owner = '{user}'))""".format(user=frappe.session.user)
        list = frappe.db.get_all('Sales Person', fields=("sales_person"),filters={"parent_sales_person":frappe.session.user})
        print(list)
        list3 = []
        for l in list:
            print(l['sales_person'])
            list3.append(l['sales_person'])
            print(list3)
            list2  = frappe.db.get_all('Sales Person', fields=("sales_person"),filters={"parent_sales_person":l['sales_person']})
            print(list2)
            for lead in list2:
                list3.append(lead['sales_person'])
                print(list3)
        print(list3)
        if len(list3)==1:
            print(len(list3))
            return "(`tabLead`.lead_owner = {user})  OR (`tabLead`.lead_owner = '{a}')".format(user=frappe.db.escape(user),a=list3[0])
            # return "((`tabLead`.lead_owner = 'milindm@switchmyloan.in') OR (`tabLead`.lead_owner = 'saksha@switchmyloan.in'))"
        elif len(list3)>1:
            print(tuple(list3))
            print(len(list3))
            return """(`tabLead`.lead_owner = {user})  OR (`tabLead`.lead_owner in {list})""".format(user=frappe.db.escape(user),list = tuple(list3))
        
        else:
            return "(`tabLead`.lead_owner = '{user}')".format(user=frappe.session.user)




