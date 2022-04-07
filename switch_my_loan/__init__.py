
__version__ = '0.1.4-uat'

import frappe
import os
import json

@frappe.whitelist()
def neodove_webhook():
    log_file_path = frappe.utils.get_files_path('neodove.json')

    logs = "[]" 
    if os.path.exists(log_file_path):
        with open(log_file_path, "r") as f:
            logs = f.read()
        f.close()
    
    logs = json.loads(logs)
    logs.append(frappe.local.form_dict)
    with open(log_file_path, "w") as f:
        f.write(json.dumps(logs))
    f.close()
    
    frappe.response.message = frappe.form_dict
