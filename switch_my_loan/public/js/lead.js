frappe.ui.form.on('Lead', {
	refresh: function(frm) {
        if(frappe.user_roles.includes('CRM User'))
        {
            frm.set_value("telecaller_name", frappe.session.user)
        }

	}
});