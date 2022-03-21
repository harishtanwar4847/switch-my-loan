Dear {{ doc.lead_name }},<br>
In order to process your file, we require the following documents    .<br><br>
Kindly click on the below link and upload the documents:    <br><br>
Or Email the documents to your relationship manager on: {{ doc.lead_owner}} <br><br>
In case of any query please contact {% set var = frappe.db.get_value("User", doc.lead_owner, "mobile_no") %} {{var}}  or write to {{ doc.lead_owner }}<br>
   <br><br>

Regards,<br><br>
Your Friendly loan buddy<br><br>
Switch My Loan Pvt. Ltd.<br>