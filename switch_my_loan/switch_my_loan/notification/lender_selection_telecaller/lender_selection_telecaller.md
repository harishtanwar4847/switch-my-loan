Lender selection:<br><br>
Dear {% set var = frappe.db.get_value("User", doc.telecaller_name, "full_name") %} {{var}},<br><br>
The lender has been selected for the customer {{doc.lead_name}}.<br><br>
Kindly login to {{frappe.get_url()}} for more updates on the lead<br><br>
Regards,<br><br>
MyCRM