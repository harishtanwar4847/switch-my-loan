import frappe

def get_user_hierarchy(table_name, field_name, parent_field, user):
    """
    Generic function to retrieve a list of users in a hierarchy.
    :param table_name: Name of the table to query (e.g., 'CRM Person', 'Sales Person').
    :param field_name: Name of the field to return (e.g., 'crm_person_name', 'sales_person').
    :param parent_field: Name of the parent field in the hierarchy.
    :param user: The user for whom to retrieve the hierarchy.
    :return: A list of users in the hierarchy.
    """
    hierarchy_list = [user]
    subordinates = [person[field_name] for person in frappe.db.get_all(table_name, fields=[field_name], filters={parent_field: user})]

    for subordinate in subordinates:
        if subordinate not in hierarchy_list:
            hierarchy_list.append(subordinate)
            further_subordinates = get_user_hierarchy(table_name, field_name, parent_field, subordinate)
            hierarchy_list.extend([user for user in further_subordinates if user not in hierarchy_list])

    return hierarchy_list

def construct_hierarchy_query(user, hierarchy_list, field_name):
    """
    Constructs an SQL query based on a user and their hierarchy.
    :param user: The current user.
    :param hierarchy_list: List of users in the hierarchy.
    :param field_name: The field name to be used in the SQL query.
    :return: An SQL query string.
    """
    if len(hierarchy_list) > 1:
        return f"(`tabLead`.{field_name} IN {tuple(hierarchy_list)})"
    else:
        return f"(`tabLead`.{field_name} = '{user}')"

def lacks_roles(user_roles, roles_to_check):
    return not any(role in user_roles for role in roles_to_check)

def has_roles(user_roles, roles_to_check):
    return any(role in user_roles for role in roles_to_check)

def lead_query(user=frappe.session.user):
    roles = frappe.get_roles(user)
    print(f"\n>>>>>>> Current User: {user} <<<<<<<\n")

    ## Skip the entire process if 'System Manager' role is present
    if 'System Manager' in roles:
        return

    # Specific user check
    if user == 'himanshu@switchmyloan.in':
        return "(`tabLead`.docstatus = 0)"

    # Role-based checks
    if 'Sales Manager' in roles:
        sales_hierarchy = get_user_hierarchy('Sales Person', 'sales_person', 'parent_sales_person', user)
        return construct_hierarchy_query(user, sales_hierarchy, 'lead_owner')
    
    if 'Sales User' in roles:
        return f"(`tabLead`.lead_owner = '{user}')"

    if 'CRM Manager' in roles:
        crm_hierarchy = get_user_hierarchy('CRM Person', 'crm_person_name', 'parent_crm_person', user)
        return construct_hierarchy_query(user, crm_hierarchy, 'telecaller_name') + " OR " + construct_hierarchy_query(user, crm_hierarchy, 'lead_owner')

    if has_roles(roles, ['CRM User', 'Partner User']):
        return f"(`tabLead`.telecaller_name = '{user}')"

    if 'Partner Manager' in roles:
        return f"(`tabLead`.telecaller_name is not null)"
