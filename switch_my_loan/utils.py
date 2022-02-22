import frappe

def workflow_states(doc, method): 
    old_doc = doc.get_doc_before_save()
    if doc.workflow_state == "Open":
        if doc.workflow_state == "Open" and old_doc == None:
            doc.append('remark', {
            'status' : 'Call Done'
    })
    # list = ["Meeting Scheduled", "Meeting Conducted", "Partly Documents Collected", "Documents Received", "Lender Selection", "Login Done", "Additional Doc Required", "Sanctioned", "Disbursement Doc List", "Disbursement doc Submitted", "Disbursed", "Amount Credited"]
    # for work in list:
    #     if doc.workflow_state == work:
    #         if doc.workflow_state != old_doc.workflow_state:
    #             doc.append('remark', {
    #         'status' : 'Meeting Remarks'
    #     })

    if doc.workflow_state == "Call Done":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : "Meeting Scheduled"
    })

    if doc.workflow_state == "Meeting Scheduled":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Meeting Conducted'
    })

    if doc.workflow_state == "Meeting Conducted":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Partly Documents Collected/Documents Received'
    })

    if doc.workflow_state == "Partly Documents Collected":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Documents Received'
    })

    if doc.workflow_state == "Documents Received":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Lender Selection'
    })

    if doc.workflow_state == "Lender Selection":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Login Done'
    })

    if doc.workflow_state == "Login Done":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Additional Doc Required'
    })

    if doc.workflow_state == "Additional Doc Required":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Sanctioned'
    })

    if doc.workflow_state == "Sanctioned":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Disbursement Doc List'
    })

    if doc.workflow_state == "Disbursement Doc List":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Disbursement Doc Submitted'
    })

    if doc.workflow_state == "Disbursement Doc Submitted":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Disbursed'
    })

    if doc.workflow_state == "Disbursed":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Amount Credited'
    })
    sales_person = frappe.db.sql("""select sales_person from `tabProduct Sales Team` where location_name = %s and from_amount <= %s and to_amount >= %s and location_parent = %s""", (doc.location,doc.loan_amount,doc.loan_amount,doc.product_required))
    if doc.telecaller_name!= None and doc.loan_amount != None and doc.location!= None and doc.product_required!= None:
        doc.lead_owner = sales_person[0][0]
        print(doc.lead_owner)
        

            

