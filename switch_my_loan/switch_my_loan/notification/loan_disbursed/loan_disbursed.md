Congratulations Dear {{ doc.lead_name}},<br><br>
We are thrilled to inform you that your loan has been disbursed by {{doc.lender_selection}}. The amount will<br><br>
be credited in your account within 2 working days / you will receive the cheque from the bank<br><br>
branch within 2 working days.<br><br>
In case of any query please contact {% set var = frappe.db.get_value("User", doc.lead_owner, "mobile_no") %} {{var}} or write to {{doc.lead_owner}}<br>
 <br><br>
For further loan requirements please visit www.switchmyloan.in<br><br>
Regards,<br><br>
Your Friendly loan buddy<br><br>
Switch My Loan Pvt. Ltd.<br>