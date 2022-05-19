Dear {% set var = frappe.db.get_value("User", doc.lead_owner, "full_name") %} {{var}},<br><br>
A meeting has been scheduled with the customer {{doc.lead_name}}. <br><br>
Their status has been changed to {{doc.status}}<br><br>
Kindly login to {{frappe.get_url()}} for more details on the lead<br><br>
Regards,<br><br>
MyCRM