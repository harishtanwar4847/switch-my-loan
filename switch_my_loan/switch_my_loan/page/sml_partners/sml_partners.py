
import frappe;
 
@frappe.whitelist()
def get_partners():
    partners = frappe.db.sql("""Select * from `tabPartners`""", as_dict=1)
    return partners;

@frappe.whitelist()
def insert_partners():
   doc = frappe.get_doc({
    "doctype": "Partners",
    "partner_id": "3",
    "first_name": "abdul",
    "last_name": "waadudh",
    "phone": "8768768877",
    "email": "abdul@codosphere.com",
    "dob": "1996-01-01",
    "pincode": "560056",
    "city": "bengaluru",
    "partner_type": "partner_corporate",
    "created_at": "2022-03-10",
    "updated_at": "2022-03-10",
    "status": "New",
   })
   doc.insert()
   return doc;

@frappe.whitelist()
def filter_by_user_type(partner_type_value, user_status_value):
  userType = partner_type_value
  status = user_status_value
  if(userType): 
    if(status):
      records = frappe.db.sql("""
        SELECT * FROM `tabPartners` WHERE `partner_type` = %s AND `status` = %s""", (userType, status), as_dict=True)
    else:
      records = frappe.db.sql("""
        SELECT * FROM `tabPartners` WHERE `partner_type` = %s""", (userType), as_dict=True)
  else:
    if(status):
      records = frappe.db.sql("""
        SELECT * FROM `tabPartners` WHERE `status` = %s""", (status), as_dict=True)
    else:
      records = frappe.db.sql("""
        SELECT * FROM `tabPartners`""", as_dict=True)
  return records;

@frappe.whitelist()
def advanced_search(field_name, field_value,created_at_start_date,created_at_end_date,enable_column1, enable_column2):
     if(enable_column1 == "true" and enable_column2 == "true"):
        records =  frappe.get_all('Partners', filters={field_name: ['like', '%{}%'.format(field_value)],'created_at': ['between', [created_at_start_date, created_at_end_date]]}, fields=["*"])
     elif(enable_column1 == "true"):
        records =  frappe.get_all('Partners', filters={field_name: ['like', '%{}%'.format(field_value)]}, fields=["*"])
     else:
        records = frappe.get_all('Partners', filters={'created_at': ['between', [created_at_start_date, created_at_end_date]]}, fields=["*"])
     return records;