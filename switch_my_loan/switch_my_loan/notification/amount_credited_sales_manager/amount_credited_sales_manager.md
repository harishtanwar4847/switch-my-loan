Dear {% set var = frappe.db.get_value("User", doc.lead_owner, "full_name") %} {{var}},<br><br>
The amount has been remitted to the customer’s {{doc.lead_name}} bank account.<br><br>
The status has been changed to {{doc.status}}<br><br>
Kindly login to {{frappe.get_url()}} for more updates on the lead<br><br>
Regards,<br><br>
MyCRM