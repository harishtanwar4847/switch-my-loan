Dear {% set var = frappe.db.get_value("User", doc.lead_owner, "full_name") %} {{var}},
A lead has been assigned to you. Kindly login to mycrm.switchmyloan.in to attend the lead.
Lead Name: {{doc.lead_name}}

Regards,
SML BUD