function get_doc_upload_link(frm) {
  const encryptionKey = CryptoJS.enc.Utf8.parse(frappe.boot?.sml_encryption_key);
  const nucleusBaseUrl = frappe.boot?.sml_nucleus_base_url;
  const token = CryptoJS.AES.encrypt(JSON.stringify({ docname: frm.docname, doctype: frm.doctype }), encryptionKey, {
    mode: CryptoJS.mode.ECB,
  }).toString();

  return `${nucleusBaseUrl}/crm/submitDocuments?token=${encodeURIComponent(token)}`;
}

frappe.ui.form.on('Lead', {
  refresh: function (frm) {
    frm.get_field('remark').grid.df.cannot_delete_rows = true;
    // frm.set_df_property("status", "read_only", 1)
    console.log('Upload Link', get_doc_upload_link(frm));
    if (frm.is_new() && (frappe.user_roles.includes('CRM User') || frappe.user_roles.includes('Partner User'))) {
      frm.set_value('telecaller_name', frappe.session.user);
    }
    if (
      (frm.is_new() && frappe.user_roles.includes('Sales User')) ||
      (frm.is_new() && frappe.user_roles.includes('Sales Manager'))
    ) {
      frm.set_value('lead_owner', frappe.session.user);
    }
    if (frappe.user_roles.includes('Sales User') && frm.is_new()) {
      frm.toggle_display('telecaller_name', false);
      frm.toggle_display('crm_team_remarks', false);
    }

    if (
      !frm.is_new() &&
      (frappe.user_roles.includes('CRM User') || frappe.user_roles.includes('Partner User')) &&
      !frappe.user_roles.includes('Sales User') &&
      !frappe.user_roles.includes('Sales Manager') &&
      frm.doc.source != 'Website' &&
      frm.doc.source != 'Website WhatsApp BOT' &&
      frm.doc.source != 'Basic Home Loan'
    ) {
      frm.toggle_display('location', false);
      frm.toggle_display('any_existing_obligations', false);
      frm.toggle_display('customer_profile', false);
      frm.toggle_display('lender_branch', false);
      frm.toggle_display('take_home_salary', false);
      frm.toggle_display('remark', false);
      frm.toggle_display('source', false);
      frm.toggle_display('partner', false);
      frm.toggle_display('do_you_own_a_car', false);
      frm.toggle_display('mandate_required', false);
      frm.toggle_display('sourcing_agent', false);
      frm.toggle_display('supplier_group', false);
      frm.toggle_display('fixed_cost', false);
      frm.toggle_display('commission_rate', false);
      frm.toggle_display('lender_selection', false);
    }

    if (frm.doc.workflow_state == 'Lender Selection' && !frm.doc.mandate_required) {
      frm.dirty();
    }

    if (frm.doc.status == 'On Hold') {
      frm.add_custom_button(
        __('Resume'),
        function () {
          frm.trigger('unhold_purchase_order');
        },
        __('Status')
      );
      frm.fields.forEach(function (l) {
        frm.set_df_property(l.df.fieldname, 'read_only', 1);
      });
    }

    if (frm.doc.status == 'Drop') {
      frm.add_custom_button(
        __('Resume'),
        function () {
          frm.trigger('unhold_purchase_order');
        },
        __('Status')
      );
      frm.fields.forEach(function (l) {
        frm.set_df_property(l.df.fieldname, 'read_only', 1);
      });
    }

    if (frm.doc.status == 'Rejected') {
      frm.add_custom_button(
        __('Reopen'),
        function () {
          frm.trigger('unclose_purchase_order');
        },
        __('Status')
      );
      frm.fields.forEach(function (l) {
        frm.set_df_property(l.df.fieldname, 'read_only', 1);
      });
    }

    if (frm.doc.status == 'Customer not reachable') {
      frm.add_custom_button(
        __('Resume'),
        function () {
          frm.trigger('unhold_purchase_order');
        },
        __('Status')
      );
      frm.fields.forEach(function (l) {
        frm.set_df_property(l.df.fieldname, 'read_only', 1);
      });
    }

    if (frm.doc.status == 'Customer not responding') {
      frm.add_custom_button(
        __('Resume'),
        function () {
          frm.trigger('unhold_purchase_order');
        },
        __('Status')
      );
      frm.fields.forEach(function (l) {
        frm.set_df_property(l.df.fieldname, 'read_only', 1);
      });
    }

    if (
      frm.doc.status != 'On Hold' &&
      frm.doc.status != 'Rejected' &&
      frm.doc.status != 'Drop' &&
      frm.doc.status != 'Customer not reachable' &&
      frm.doc.status != 'Customer not responding'
    ) {
      frm.fields.forEach(function (l) {
        frm.set_df_property(l.df.fieldname, 'read_only', 0);
      });
    }

    if (
      !frm.doc.__islocal &&
      frm.doc.status != 'On Hold' &&
      frm.doc.status != 'Rejected' &&
      frm.doc.status != 'Drop' &&
      frm.doc.status != 'Customer not reachable' &&
      frm.doc.status != 'Customer not responding' &&
      (frappe.user_roles.includes('Sales User') || frappe.user_roles.includes('Sales Manager'))
    ) {
      frm.add_custom_button(
        __('On Hold'),
        function () {
          frm.trigger('hold_purchase_order');
        },
        __('Status')
      );

      frm.add_custom_button(
        __('Drop'),
        function () {
          frm.trigger('drop_purchase_order');
        },
        __('Status')
      );

      frm.add_custom_button(
        __('Reject'),
        function () {
          frm.trigger('close_purchase_order');
        },
        __('Status')
      );

      frm.add_custom_button(
        __('Customer not reachable'),
        function () {
          frm.trigger('customer_not_reachable');
        },
        __('Status')
      );

      frm.add_custom_button(
        __('Customer not responding'),
        function () {
          frm.trigger('customer_not_responding');
        },
        __('Status')
      );
    }
    frm.cscript.custom_refresh = function (doc) {
      if (
        frappe.user_roles.includes('Sales User') &&
        !frappe.user_roles.includes('System Manager') &&
        !(frm.doc.workflow_state == 'Open')
      ) {
        frm.set_df_property('telecaller_name', 'read_only', doc.__islocal ? 0 : 1);
        frm.set_df_property('crm_team_remarks', 'read_only', doc.__islocal ? 0 : 1);
      }
    };
    if (
      !frm.doc.__islocal &&
      frm.doc.status != 'On Hold' &&
      frm.doc.status != 'Customer not reachable' &&
      frm.doc.status != 'Customer not responding' &&
      frm.doc.status != 'Rejected' &&
      frm.doc.status != 'Drop' &&
      frm.doc.workflow_state == 'Open' &&
      frm.doc.source.includes('Website') &&
      frappe.user_roles.includes('CRM User') &&
      !frappe.user_roles.includes('Sales User')
    ) {
      frm.add_custom_button(
        __('On Hold'),
        function () {
          frm.trigger('hold_purchase_order');
        },
        __('Status')
      );

      frm.add_custom_button(
        __('Drop'),
        function () {
          frm.trigger('drop_purchase_order');
        },
        __('Status')
      );

      frm.add_custom_button(
        __('Reject'),
        function () {
          frm.trigger('close_purchase_order');
        },
        __('Status')
      );

      frm.add_custom_button(
        __('Customer not reachable'),
        function () {
          frm.trigger('customer_not_reachable');
        },
        __('Status')
      );

      frm.add_custom_button(
        __('Customer not responding'),
        function () {
          frm.trigger('customer_not_responding');
        },
        __('Status')
      );
    }

    if (
      frappe.user_roles.includes('CRM User') &&
      !frappe.user_roles.includes('Sales User') &&
      !frappe.user_roles.includes('System Manager') &&
      frm.doc.source.includes('Website')
    ) {
      frm.set_df_property('source', 'read_only', 1);
    }
  },

  checklist: function (frm) {
    if (frm.doc.checklist) {
      frm.clear_table('documents');
      frappe.model.with_doc('Document Checklist', frm.doc.checklist, function () {
        let source_doc = frappe.model.get_doc('Document Checklist', frm.doc.checklist);
        $.each(source_doc.list_of_document, function (index, source_row) {
          var addChild = frm.add_child('documents');
          addChild.document = source_row.document_name;
          frm.refresh_field('documents');
        });
      });
    }
    if (!frm.doc.checklist) {
      frm.clear_table('documents');
      frm.refresh_field('documents');
    }
  },

  setup(frm) {
    frm.set_query('location', () => {
      return {
        filters: {
          is_group: ['!=', 1],
        },
      };
    });
    frm.set_query('partner', () => {
      return {
        filters: {
          customer_group: 'Partner',
        },
      };
    });
    frm.set_query('lender_selection', () => {
      return {
        filters: {
          customer_group: 'Lender',
        },
      };
    });
    frm.set_query('lender_branch', () => {
      return {
        filters: {
          is_group: ['!=', 1],
        },
      };
    });
    frm.get_field('remark').grid.cannot_add_rows = true;

    frm.set_query('investment_type', 'investment', () => {
      return {
        filters: {
          name: [
            'not in',
            frm.doc.investment.map(function (cur_seg) {
              return cur_seg.investment_type;
            }),
          ],
        },
      };
    });
  },

  validate(frm) {
    if (frm.doc.location == 'All Territories') {
      frappe.throw('Please Select Location Name');
    }
    if (frm.doc.lender_branch == 'All Territories') {
      frappe.throw('Please Select Lender Branch');
    }
    if (frm.doc.mobile_number && !/^\d{10}$/.test(frm.doc.mobile_number)) {
      frappe.throw('Mobile Number must containt 10 digits');
    }
  },

  unhold_purchase_order(frm) {
    frappe.call({
      method: 'switch_my_loan.utils.update_status',
      args: {
        lead: frm.doc.name,
        status: frm.doc.workflow_state,
      },
      callback: function (r) {
        frm.reload_doc();
      },
    });
  },
  close_purchase_order(frm) {
    var me = this;
    var d = new frappe.ui.Dialog({
      title: __('Reason for Rejection'),
      fields: [
        {
          fieldname: 'reason_for_rejection',
          fieldtype: 'Text',
          reqd: 1,
        },
      ],
      primary_action: function () {
        var data = d.get_values();
        let reason_for_rejection = 'Reason for Rejection: ' + data.reason_for_rejection;

        frappe.call({
          method: 'frappe.desk.form.utils.add_comment',
          args: {
            reference_doctype: frm.doc.doctype,
            reference_name: frm.doc.name,
            content: __(reason_for_rejection),
            comment_email: frappe.session.user,
            comment_by: frappe.session.user_fullname,
          },
          callback: function (r) {
            if (!r.exc) {
              console.log('testing');
              frappe.call({
                method: 'switch_my_loan.utils.update_status',
                args: {
                  lead: frm.doc.name,
                  status: 'Rejected',
                },
                callback: function (r) {
                  frm.reload_doc();
                },
              });

              d.hide();
            }
          },
        });
      },
    });
    d.show();
  },

  unclose_purchase_order(frm) {
    frappe.call({
      method: 'switch_my_loan.utils.update_status',
      args: {
        lead: frm.doc.name,
        status: frm.doc.workflow_state,
      },
      callback: function (r) {
        frm.reload_doc();
      },
    });
  },

  hold_purchase_order(frm) {
    var me = this;
    var d = new frappe.ui.Dialog({
      title: __('Reason for Hold'),
      fields: [
        {
          fieldname: 'reason_for_hold',
          fieldtype: 'Text',
          reqd: 1,
        },
      ],
      primary_action: function () {
        var data = d.get_values();
        let reason_for_hold = 'Reason for hold: ' + data.reason_for_hold;

        frappe.call({
          method: 'frappe.desk.form.utils.add_comment',
          args: {
            reference_doctype: frm.doc.doctype,
            reference_name: frm.doc.name,
            content: __(reason_for_hold),
            comment_email: frappe.session.user,
            comment_by: frappe.session.user_fullname,
          },
          callback: function (r) {
            if (!r.exc) {
              console.log('testing');
              frappe.call({
                method: 'switch_my_loan.utils.update_status',
                args: {
                  lead: frm.doc.name,
                  status: 'On Hold',
                },
                callback: function (r) {
                  frm.reload_doc();
                },
              });

              d.hide();
            }
          },
        });
      },
    });
    d.show();
  },

  drop_purchase_order(frm) {
    var me = this;
    var d = new frappe.ui.Dialog({
      title: __('Reason for Drop'),
      fields: [
        {
          fieldname: 'reason_for_drop',
          fieldtype: 'Select',
          options: ['Not Interested', 'Not Eligible', 'Not Connected'],
          reqd: 1,
        },
      ],
      primary_action: function () {
        console.log(frm);
        var data = d.get_values();
        let reason_for_drop = 'Reason for drop: ' + data.reason_for_drop;
        if (window.timeout) {
          clearTimeout(window.timeout);
          delete window.timeout;
        }
        window.timeout = setTimeout(function () {
          frm.set_value('reason_for_drop', data.reason_for_drop);
          frm.refresh_field('reason_for_drop');
          frm.save();
        }, 1500);
        // frappe.call({
        //     url: "/api/resource/Lead/"+frm.doc.name,
        //     method: "PUT",
        //     args: {
        //         reason_for_drop: data.reason_for_drop
        //     },
        //     callback: function(r){
        //         console.log("reloading form")
        //         frm.reload()
        //     }
        // })
        frappe.call({
          method: 'frappe.desk.form.utils.add_comment',
          args: {
            reference_doctype: frm.doc.doctype,
            reference_name: frm.doc.name,
            content: __(reason_for_drop),
            comment_email: frappe.session.user,
            comment_by: frappe.session.user_fullname,
          },
          callback: function (r) {
            if (!r.exc) {
              console.log('testing');
              frappe.call({
                method: 'switch_my_loan.utils.update_status',
                args: {
                  lead: frm.doc.name,
                  status: 'Drop',
                },
                callback: function (r) {
                  frm.reload_doc();
                },
              });
              d.hide();
            }
          },
        });
        // if(frm.doc.status == "Drop"){
        //     frm.set_value("reason_for_drop", data.reason_for_drop)
        //     cur_frm.save()
        // }
      },
    });
    d.show();
  },

  customer_not_reachable(frm) {
    frappe.call({
      method: 'switch_my_loan.utils.update_status',
      args: {
        lead: frm.doc.name,
        status: 'Customer not reachable',
      },
      callback: function (r) {
        frm.reload_doc();
      },
    });
  },

  customer_not_responding(frm) {
    frappe.call({
      method: 'switch_my_loan.utils.update_status',
      args: {
        lead: frm.doc.name,
        status: 'Customer not responding',
      },
      callback: function (r) {
        frm.reload_doc();
      },
    });
  },

  after_save(frm) {
    // Updating the Docs Upload Link for the Lead
    frappe.db.set_value(frm.doctype, frm.docname, 'docs_upload_link', get_doc_upload_link(frm));
  },

  // Setting the Umbrella Source Based on the Source and if umbrella source is found then disable the Umbrella Source
  async source(frm) {
    const { message } = await frappe.db.get_value('Lead Source', { name: frm.doc.source }, ['umbrella_source']);
    frm.set_value('umbrella_source', message.umbrella_source || '');
  },
});
