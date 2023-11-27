// Copyright (c) 2023, Atrina Technologies Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pre Lead', {
	// refresh: function(frm) {

	// }

	after_save(frm) {
		frappe.call({
			method: "switch_my_loan.switch_my_loan.doctype.pre_lead.pre_lead.log_status",
			args: { pre_lead_id: frm.doc.name, status: frm.doc.status },
			callback: function (r) {
				location.reload();
			}
		});
	},
});
