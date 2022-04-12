import frappe

def execute():
    path = ''
    server_type = frappe.get_site_config().server_type
    if server_type in ('Dev', 'QA', 'UAT'):
        path = frappe.get_app_path("switch_my_loan", "patches", "notifications_imports", "email_account_dev.csv")
    elif server_type in ('Prod'):
        path = frappe.get_app_path("switch_my_loan", "patches", "notifications_imports", "email_account_sml.csv")
        domain_path = frappe.get_app_path("switch_my_loan", "patches", "notifications_imports", "email_domain_sml.csv")
        frappe.core.doctype.data_import.data_import.import_file("Email Domain", domain_path, "Insert", console=True)
    print(path)
    frappe.core.doctype.data_import.data_import.import_file("Email Account", path, "Update", console=True)