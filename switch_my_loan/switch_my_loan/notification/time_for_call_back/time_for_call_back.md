Dear {% set var = frappe.db.get_value("User", doc.lead_owner, "full_name") %} {{var}},<br><br>



The lead {{doc.name}}, {{doc.lead_name}} is due for follow up. Please update the status of the lead<br>

Click on the below link to log in to MyCRM<br>

https://mycrm.switchmyloan.in/app/lead/{{doc.name}}<br><br>



Regards,<br>

MyCRM