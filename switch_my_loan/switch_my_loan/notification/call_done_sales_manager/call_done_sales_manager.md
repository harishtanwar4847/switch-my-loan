Dear {% set var = frappe.db.get_value("User", doc.lead_owner, "full_name") %} {{var}},<br><br>
The customer {{doc.lead_name}} has been called up. Their status has been changed to {{doc.status}}<br><br>
Kindly login to {{frappe.get_url()}} for more updates on the lead<br><br>
Regards,<br><br>
MyCRM