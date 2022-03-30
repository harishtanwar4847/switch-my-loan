Congratulation {{ doc.lead_name }},<br>
We are pleased to inform you that your file has been shared with {{ doc.lender_selection}}. You will be updated<br>
once the application has been logged in.<br><br>
In case of any queries, please contact {% set var = frappe.db.get_value("User", doc.lead_owner, "full_name") %} {{var}} & 
{% set var = frappe.db.get_value("User", doc.lead_owner, "mobile_no") %} {{var}}  or write to us at {{doc.lead_owner}}<br><br>
Regards,<br><br>
Your Friendly loan buddy<br><br>

Switch My Loan Pvt. Ltd.<br>