Dear {{ doc.lead_name }},<br>
Congratulations !!!<br>
We are thrilled to inform your file has been successfully logged in, in {{ doc.lender_selection}}. We will keep<br>
you updated with the progress on your loan application.<br><br>
In case of any query please contact {% set var = frappe.db.get_value("User", doc.lead_owner, "full_name") %} {{var}} & 
{% set var = frappe.db.get_value("User", doc.lead_owner, "mobile_no") %} {{var}} or write us on {{doc.lead_owner}}, 
he will be your relationship manager.<br><br>
Regards,<br><br>
Your Friendly loan buddy<br>
Switch My Loan Pvt. Ltd.<br>