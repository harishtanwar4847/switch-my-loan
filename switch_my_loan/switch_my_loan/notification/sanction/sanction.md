Congratulations Mr. {{ doc.lead_name }}, your loan application has been sanctioned by {{doc.lender_selection}} . You will receive an email with the list of documents required for disbursing the loan. Kindly share those documents at the earliest to avoid any delay. In case of any query please contact us on {% set var = frappe.db.get_value("User", doc.lead_owner, "mobile_no") %} {{var}} or write to info@switchmyloan.in -Switch My Loan