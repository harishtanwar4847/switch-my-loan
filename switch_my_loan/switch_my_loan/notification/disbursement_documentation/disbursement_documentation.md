Dear Mr. {{ doc.lead_name }}, You must have received a mail from SML, with the list of documents to be shared to disburse your loan. 
Kindly click on the below link 
{{ doc.docs_upload_link }}  
and upload the required documents for a quick disbursal of your loan.
In case of any query please contact {% set var = frappe.db.get_value("User", doc.lead_owner, "mobile_no") %} {{var}} or write to info@switchmyloan.in -Switch My Loan