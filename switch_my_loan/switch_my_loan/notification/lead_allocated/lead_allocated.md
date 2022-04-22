Dear {% set var = frappe.db.get_value("User", doc.lead_owner, "full_name") %} {{var}},<br><br>
Lead of {{doc.lead_name}} with Lead ID {{doc.name}} has been allocated to you.<br>
Kindly attend to the lead and update the status within 2 hours.<br><br>

Best Regards,<br>
CRM Team.