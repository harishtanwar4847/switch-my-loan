frappe.ui.form.on('Lead', {
	refresh: function(frm) {

        frm.get_field("remark").grid.df.cannot_delete_rows = true;

        if(frm.is_new() && frappe.user_roles.includes('CRM User'))
        {
            frm.set_value("telecaller_name", frappe.session.user)
        }
        if((frm.is_new() && frappe.user_roles.includes('Sales User')) || (frm.is_new() && frappe.user_roles.includes('Sales Manager')))
        {
            frm.set_value("lead_owner", frappe.session.user)        
        }
        if(frappe.user_roles.includes('Sales User') && frm.is_new()){
            frm.toggle_display("telecaller_name",false)
            frm.toggle_display("crm_team_remarks",false)


        }

        
        if(!frm.is_new() && frappe.user_roles.includes('CRM User') && !frappe.user_roles.includes('Sales User') && !frappe.user_roles.includes('Sales Manager')){
            frm.toggle_display("location",false)
            frm.toggle_display("any_existing_obligations",false)
            frm.toggle_display("customer_profile",false)
            frm.toggle_display("lender_branch",false)
            frm.toggle_display("take_home_salary",false)
            frm.toggle_display("remark",false)
            frm.toggle_display("source",false)
            frm.toggle_display("partner",false)
            frm.toggle_display("mobile_number",false)
            frm.toggle_display("email_id",false)
        }


        if(frm.doc.workflow_state == "Lender Selection" && !frm.doc.mandate_required){
            frm.dirty()
        }


        
        if(frm.doc.status == "On Hold"){
            frm.add_custom_button(__('Resume'), function(){
                frm.trigger("unhold_purchase_order")
            }, __("Status"));
            frm.fields.forEach(function(l){ frm.set_df_property(l.df.fieldname, "read_only", 1); })  
        }
        
        if(frm.doc.status == "Rejected"){
            frm.add_custom_button(__('Reopen'), function(){    
                    frm.trigger("unclose_purchase_order")
                }, __("Status"));
            frm.fields.forEach(function(l){ frm.set_df_property(l.df.fieldname, "read_only", 1); })  
        }
        if(frm.doc.status != "On Hold" && frm.doc.status != "Rejected"){
            frm.fields.forEach(function(l){ frm.set_df_property(l.df.fieldname, "read_only", 0); })  
        }
        

        if(!frm.doc.__islocal && frm.doc.status != "On Hold" && frm.doc.status != "Rejected" && (frappe.user_roles.includes('Sales User') || frappe.user_roles.includes('Sales Manager'))){
            frm.add_custom_button(__('On Hold'), function(){
                frm.trigger("hold_purchase_order")                
            }, __("Status"));
        
            frm.add_custom_button(__('Reject'), function(){
                frm.trigger("close_purchase_order")
            }, __("Status"));
        }
        frm.cscript.custom_refresh = function(doc) {
            if(frappe.user_roles.includes('Sales User')){
                frm.set_df_property("telecaller_name", "read_only", doc.__islocal ? 0 : 1);
                frm.set_df_property("crm_team_remarks", "read_only", doc.__islocal ? 0 : 1);


            }
        }

  
    },

    checklist: function (frm) {
        if (frm.doc.checklist) {
            frm.clear_table('documents');
            frappe.model.with_doc('Document Checklist', frm.doc.checklist, function () {
                let source_doc = frappe.model.get_doc('Document Checklist', frm.doc.checklist);
                $.each(source_doc.list_of_document, function (index, source_row) {
                    
                var addChild = frm.add_child("documents");
	             	addChild.document = source_row.document_name;
		            frm.refresh_field('documents');
                });
            });
        }
        if(!frm.doc.checklist) {
            frm.clear_table('documents');
            frm.refresh_field('documents');
        }
    },

    setup(frm) {
        frm.set_query('location', () => {
            return {
                filters: {
                    is_group:['!=',1]
                }
            }
        })
        frm.set_query('lender_branch', () => {
            return {
                filters: {
                    is_group:['!=',1]
                }
            }
        })
	    frm.get_field('remark').grid.cannot_add_rows = true;
        
        },

    validate(frm){
        if(frm.doc.location == "All Territories"){
            frappe.throw("Please Select Location Name")
        }
        if(frm.doc.lender_branch == "All Territories"){
            frappe.throw("Please Select Lender Branch")
        }
    },

    unhold_purchase_order(frm){
        frappe.call({
            "method":"switch_my_loan.utils.update_status",
            args:{
                lead:frm.doc.name,
                status:frm.doc.workflow_state
            },
            callback:function(r){
                frm.reload_doc()
            }
        })
	},
    close_purchase_order(frm){
        frappe.call({
            "method":"switch_my_loan.utils.update_status",
            args:{
                lead:frm.doc.name,
                status:"Rejected"
            },
            callback:function(r){
                frm.reload_doc()
            }
        })
	},

    unclose_purchase_order(frm){
        frappe.call({
            "method":"switch_my_loan.utils.update_status",
            args:{
                lead:frm.doc.name,
                status:frm.doc.workflow_state
            },
            callback:function(r){
                frm.reload_doc()
            }
        })
	},


    hold_purchase_order(frm){
		var me = this;
		var d = new frappe.ui.Dialog({
			title: __('Reason for Hold'),
			fields: [
				{
					"fieldname": "reason_for_hold",
					"fieldtype": "Text",
					"reqd": 1,
				}
			],
			primary_action: function() {
				var data = d.get_values();
				let reason_for_hold = 'Reason for hold: ' + data.reason_for_hold;

				frappe.call({
					method: "frappe.desk.form.utils.add_comment",
					args: {
						reference_doctype: frm.doc.doctype,
						reference_name: frm.doc.name,
						content: __(reason_for_hold),
						comment_email: frappe.session.user,
						comment_by: frappe.session.user_fullname
					},
					callback: function(r) {
						if(!r.exc) {
                            console.log("testing")
                            frappe.call({
                                "method":"switch_my_loan.utils.update_status",
                                args:{
                                    lead:frm.doc.name,
                                    status:"On Hold"
                                },
                                callback:function(r){
                                    frm.reload_doc()
                                }
                            })
                            
							d.hide();
                            
						}
					}
				});
			}
		});
		d.show();
	},


});










