// Copyright (c) 2022, Atrina Technologies Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Product', {
	// refresh: function(frm) {
	// }
	
	setup(frm){
		frm.set_query('location_name', 'product_sales_team', () => {
			return {
				filters: {
					is_group:['!=',1]
				}
			}
		})

	}
});

frappe.ui.form.on('Product Sales Team',{
	product_sales_team_add(frm,cdt,cdn){
		var row = locals[cdt][cdn]
		row.location_name = ""
	}
})



