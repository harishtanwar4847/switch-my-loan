import frappe

def execute():
    custom_fields = ["Lead-loan_type", "Lead-outstanding_amount", "Lead-lender_name", "Lead-current_emi", "Lead-current_roi", "Lead-no_of_emis_paid"]
    for field in custom_fields:  
        try:
            frappe.delete_doc("Custom Field", field)
        except frappe.DuplicateEntryError:
            pass