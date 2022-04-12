// Copyright (c) 2022, Atrina Technologies Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Document Checklist', {
	// refresh: function(frm) {

	// }
	setup: function(frm){
		frm.set_query('document_name', 'list_of_document', () => {
            return {
                filters: {
                    //["Segment", "name", "!=", "NSE-Cash"]
                    'name':['not in', frm.doc.list_of_document.map(function(cur_seg){return cur_seg.document_name})],

                }
            }
        })      
	}
});
