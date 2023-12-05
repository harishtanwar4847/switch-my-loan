
import frappe;
 
@frappe.whitelist()
def get_partner_details(partner_id):
    return frappe.db.sql("""Select * from `tabPartners` WHERE `partner_id` = %s""", (partner_id), as_dict=1)