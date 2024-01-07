# Copyright (c) 2024, Atrina Technologies Pvt Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Lenders(Document):
	pass

def on_update(doc, method):
    current_doc = doc.get_doc_before_save()
    
    if(current_doc.status != doc.status):
        doc.updated_at = frappe.utils.now_datetime().replace(microsecond=0)
 