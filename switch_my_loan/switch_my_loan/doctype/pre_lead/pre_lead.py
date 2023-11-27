# Copyright (c) 2023, Atrina Technologies Pvt Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PreLead(Document):
	pass

@frappe.whitelist()
def log_status(pre_lead_id, status):
	doc = frappe.get_doc("Pre Lead", pre_lead_id)
	doc.append("pre_lead_disposition", {
		"updated_by": frappe.session.user,
		"updated_at": frappe.utils.now(),
		"status": status,
	})
	doc.save()
	return True