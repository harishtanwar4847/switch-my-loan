import frappe
from frappe.core.doctype.data_import.data_import import import_file

def execute():
    path = frappe.get_app_path('switch_my_loan','patches','lead_workflow3','workflow_state.csv')
    import_file('Workflow State', path, 'Insert',console=True)
    path = frappe.get_app_path('switch_my_loan','patches','lead_workflow3','workflow_action_master.csv')
    import_file('Workflow Action Master', path, 'Insert',console=True)
    path = frappe.get_app_path('switch_my_loan','patches','lead_workflow3','workflow.csv')
    import_file('Workflow', path, 'Insert',console=True)
