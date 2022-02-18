frappe.ui.form.on('Lead', {
	refresh: function(frm) {
        if(frappe.user_roles.includes('CRM User'))
        {
            frm.set_value("telecaller_name", frappe.session.user)
        }
        if(frappe.user_roles.includes('Sales User') || frappe.user_roles.includes('Sales Manager'))
        {
            frm.set_value("lead_owner", frappe.session.user)
        }

    },

});



