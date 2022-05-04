Login done:<br><br>
Dear {% set var = frappe.db.get_value("User", doc.telecaller_name, "full_name") %} {{var}},<br><br>
The customer {{doc.lead_name}}’s loan application has been logged in<br><br>
Kindly login to {{frappe.get_url()}} for more updates on the lead<br><br>
Regards,<br><br>
MyCRM