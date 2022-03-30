Dear {{ doc.lead_name }},<br><br>
Thank you for meeting {% set var = frappe.db.get_value("User", doc.lead_owner, "full_name") %} {{var}}  Hope we were able to answer all your queries and<br>
fulfill your requirements. For further details please contact {% set var = frappe.db.get_value("User", doc.lead_owner, "full_name") %} {{var}} and 
{% set var = frappe.db.get_value("User", doc.lead_owner, "mobile_no") %} {{var}}. He<br> 
will be your relationship manager.<br><br>
Please visit www.switchmyloan.in to know more about our products. You sit back and relax, while<br>
we do all the hard-work for your loan.<br><br>
Regards,<br><br>
Your Friendly loan buddy<br><br>
Switch My Loan Pvt. Ltd.<br>