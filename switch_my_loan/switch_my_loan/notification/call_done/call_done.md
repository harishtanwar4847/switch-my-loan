Dear {{ doc.lead_name}},
Thank you for connecting with {% set var = frappe.db.get_value("User", doc.lead_owner, "full_name") %} {{var}} . We will keep you posted with further<br>
movement on your loan application. For more details please visit us www.switchmyloan.in<br><br>
Our processes are completely digitized. You sit back and relax, while we do all the hard-work for<br>
your loan.<br><br>
Kindly rate your experience with {% set var = frappe.db.get_value("User", doc.lead_owner, "full_name") %} {{var}} on a scale of 1 to 10, 1 being Disappointing<br>
and 10 being informative and helpful.<br><br><br>

Regards,<br><br>
Your Friendly loan buddy<br><br>
Switch My Loan Pvt. Ltd.<br><br>