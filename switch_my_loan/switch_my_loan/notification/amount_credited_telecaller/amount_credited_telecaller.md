Amount Remitted:<br><br>
Dear {% set var = frappe.db.get_value("User", doc.telecaller_name, "full_name") %} {{var}},<br><br>
The amount has been remitted to the customer’s {{doc.lead_name}} bank account<br><br>
Kindly login to {{frappe.get_url()}} for more updates on the lead<br><br>
Regards,<br><br>
MyCRM