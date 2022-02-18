// Copyright (c) 2022, Atrina Technologies Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Product', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Product Sales Team', {
	product_sales_team_add: function(frm,cdt,cdn) {
	var u = locals[cdt][cdn];
    u['location_parent'] = frm.doc.product_name
	}
});


