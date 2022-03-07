import frappe

def workflow_states(doc,method): 
    old_doc = doc.get_doc_before_save()
    if doc.workflow_state == "Open":
        if doc.workflow_state == "Open" and old_doc == None:
            doc.append('remark', {
            'status' : 'Call Done'
    })

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
    user = frappe.session.user
    if 'CRM User' in frappe.get_roles(user) and doc.loan_amount == None:
        frappe.throw("Please Enter Loan Amount")

    if 'CRM User' in frappe.get_roles(user) and doc.location == None:
        frappe.throw("Please Enter Location")
    
    if 'CRM User' in frappe.get_roles(user) and doc.product_required == None:
        frappe.throw("Please Enter Product Required")
    
    
    
    sales_person = frappe.db.sql("""select sales_person from `tabProduct Sales Team` where location_name = %s and from_amount <= %s and to_amount >= %s and location_parent = %s""", (doc.location,doc.loan_amount,doc.loan_amount,doc.product_required))
    
    if 'CRM User' in frappe.get_roles(user) and doc.loan_amount != None and doc.location!= None and doc.product_required!= None:
        abc = frappe.db.get_list("Lead", filters={'workflow_state':('not in',('Amount Credited')),"lead_owner":sales_person[0][0]}, fields=("lead_owner"))
        res = [d['lead_owner'] for d in abc]
        count = res.count(doc.lead_owner)
        lead_count1 = frappe.db.sql("""select leads_count from `tabSales Person` where name = %s""", (sales_person[0][0]))
        if res.count(doc.lead_owner) <= int(lead_count1[0][0]):
            doc.lead_owner = sales_person[0][0]


    if 'CRM User' in frappe.get_roles(user) and doc.loan_amount != None and doc.location!= None and doc.product_required!= None:
        reporting_manager = frappe.db.sql("""select parent_sales_person from `tabSales Person` where name = %s""", (sales_person[0][0]))
        abc2 = frappe.db.get_list("Lead", filters={'workflow_state':('not in',('Amount Credited')),"lead_owner":reporting_manager[0][0]}, fields=("lead_owner"))
        res2 = [d['lead_owner'] for d in abc2]
        count2 = res2.count(reporting_manager[0][0])
        reporting_manager2 = frappe.db.sql("""select parent_sales_person from `tabSales Person` where name = %s""", (reporting_manager[0][0]))

        lead_count2 = frappe.db.sql("""select leads_count from `tabSales Person` where name = %s""", (reporting_manager[0][0]))

        if count2 >= int(lead_count2[0][0]):
            frappe.msgprint("Already 15 Leads Assigned, So this lead is assigned to reporting manager")
            doc.lead_owner = reporting_manager2[0][0]


    if 'CRM User' in frappe.get_roles(user) and doc.loan_amount != None and doc.location!= None and doc.product_required!= None:
        abc = frappe.db.get_list("Lead", filters={'workflow_state':('not in',('Amount Credited')),"lead_owner":sales_person[0][0]}, fields=("lead_owner"))
        res = [d['lead_owner'] for d in abc]
        count = res.count(doc.lead_owner)
        
        lead_count1 = frappe.db.sql("""select leads_count from `tabSales Person` where name = %s""", (sales_person[0][0]))
        reporting_manager = frappe.db.sql("""select parent_sales_person from `tabSales Person` where name = %s""", (sales_person[0][0]))


        if res.count(doc.lead_owner) >= int(lead_count1[0][0]):
            frappe.msgprint("Already 15 Leads Assigned, So this lead is assigned to reporting manager")
            doc.lead_owner = reporting_manager[0][0]

    
@frappe.whitelist()
def update_status(lead,status):
    doc = frappe.get_doc("Lead",lead)
    doc.set_status(update = True, status = status)
    doc.reload()




        


        

            

