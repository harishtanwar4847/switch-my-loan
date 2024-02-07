import frappe
import json
from frappe.desk.reportview import export_query as original_export_query

def get_formatted_field_arr(fields):
    return [f"`tab{doctype}`.`{field_name}`" for doctype, field_name in fields]

def get_restricted_fields(doctype=None):
  fields = frappe.db.get_list('Restricted Export Fields', 
    filters={'source_doctype': doctype}, 
    fields=['source_doctype', 'field'], 
    as_list=True
  )
  return get_formatted_field_arr(fields)

@frappe.whitelist()
def export_query(*args, **kwargs):
    user = frappe.session.user;
    roles = frappe.get_roles(user);

    # Check if the user has the 'Restrict Export' role
    if "Restrict Fields Export" in roles:
      export_payload = frappe.form_dict;
      # Get the restricted fields from the database
      restricted_fields = get_restricted_fields(export_payload['doctype']);

      # Parse the 'fields' argument from JSON to a Python list
      fields = json.loads(export_payload['fields']);

      # Remove restricted fields from the fields list
      fields = [field for field in fields if field not in restricted_fields];

      # Convert the fields list back to JSON and update kwargs
      frappe.form_dict['fields'] = json.dumps(fields);
      kwargs['fields'] = json.dumps(fields);

    # Call the original export_query with modified args or kwargs
    return original_export_query(*args, **kwargs)