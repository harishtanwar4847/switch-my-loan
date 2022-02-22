frappe.ui.form.on('Lead', {
	refresh: function(frm) {
        console.log("abc")
        if(frm.is_new() && frappe.user_roles.includes('CRM User'))
        {
            frm.set_value("telecaller_name", frappe.session.user)
        }
        if((frm.is_new() && frappe.user_roles.includes('Sales User')) || (frm.is_new() && frappe.user_roles.includes('Sales Manager')))
        {
            frm.set_value("lead_owner", frappe.session.user)
            
        }

    }

});



