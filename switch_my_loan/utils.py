import frappe
from datetime import datetime

def workflow_states(doc,method): 
    old_doc = doc.get_doc_before_save()
    # if doc.workflow_state == "Open":
    #     todayDateStr = datetime.strptime(frappe.utils.now(), "%Y-%m-%d %H:%M:%S.%f")
    #     print(todayDateStr)
    #     doc.open_time = frappe.utils.now()
    
    if doc.workflow_state == "Open" and old_doc == None:
        res = frappe.db.sql("""select count(name) from `tabLead` where product_required = %s and mobile_number = %s""",(doc.product_required,doc.mobile_number))
        no_of_results = res[0][0]
        if (no_of_results >= 1):
            frappe.throw("A Lead already with same product and mobile number")
        doc.append('remark', {
        'status' : 'Call Done'
    })
        d = datetime.now().replace(microsecond=0)
        doc.open_time = d
        # doc.save()
        # doc.reload()

    if doc.workflow_state == "Call Done":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : "Meeting Scheduled"
    })
            d = datetime.now().replace(microsecond=0)
            doc.call_done_time = d



    if doc.workflow_state == "Meeting Scheduled":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Meeting Conducted'
    })
            d = datetime.now().replace(microsecond=0)
            doc.meeting_scheduled_time = d
            # doc.save()



    if doc.workflow_state == "Meeting Conducted":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Partly Documents Collected/Documents Received'
    })
            d = datetime.now().replace(microsecond=0)
            doc.meeting_conducted_time = d
        


    if doc.workflow_state == "Partly Documents Collected":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Documents Received'
    })
            d = datetime.now().replace(microsecond=0)
            doc.partly_documents_collected_time = d


    if doc.workflow_state == "Documents Received":
        if doc.workflow_state != old_doc.workflow_state:
            doc.documents_received_time = frappe.utils.now()
            doc.append('remark', {
            'status' : 'Lender Selection'
    })
            d = datetime.now().replace(microsecond=0)
            doc.documents_received_time = d

    if doc.workflow_state == "Lender Selection":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Login Done'
    })
            d = datetime.now().replace(microsecond=0)
            doc.lender_selection_time = d
    
    if doc.workflow_state == "Pending For Reporting Manager Approval":
        if doc.workflow_state != old_doc.workflow_state:
            d = datetime.now().replace(microsecond=0)
            doc.pending_for_reporting_manager_approval_time = d


    if doc.workflow_state == "Login Done":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Additional Doc Required'
    })
            d = datetime.now().replace(microsecond=0)
            doc.login_done_time = d


    if doc.workflow_state == "Additional Doc Required":
        if doc.workflow_state != old_doc.workflow_state:
            doc.append('remark', {
            'status' : 'Sanctioned'
    })
            d = datetime.now().replace(microsecond=0)
            doc.additional_doc_required_time = d


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
            d = datetime.now().replace(microsecond=0)
            doc.disbursement_doc_list_time = d



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
            d = datetime.now().replace(microsecond=0)
            doc.disbursed_time = d


    if doc.workflow_state == "Amount Credited":
        if doc.workflow_state != old_doc.workflow_state:
            d = datetime.now().replace(microsecond=0)
            doc.amount_credited_time = d
    
   

    
    
    user = frappe.session.user
    if 'CRM User' in frappe.get_roles(user) and not 'Sales User' in frappe.get_roles(user) and not 'Sales Manager' in frappe.get_roles(user) and doc.loan_amount == None:
        frappe.throw("Please Enter Loan Amount")

    if 'CRM User' in frappe.get_roles(user) and not 'Sales User' in frappe.get_roles(user) and not 'Sales Manager' in frappe.get_roles(user) and doc.location == None:
        frappe.throw("Please Enter Location")
    
    if 'CRM User' in frappe.get_roles(user) and not 'Sales User' in frappe.get_roles(user) and not 'Sales Manager' in frappe.get_roles(user) and doc.product_required == None:
        frappe.throw("Please Enter Product Required")
    
    
    
    sales_person = frappe.db.sql("""select sales_person from `tabProduct Sales Team` where location_name = %s and amount_threshold >= %s and parent = %s order by amount_threshold asc limit 1""", (doc.location,doc.loan_amount,doc.product_required))
    # abc = frappe.db.get_list("Lead", filters={'workflow_state':('not in',('Amount Credited')),"lead_owner":sales_person[0][0]}, fields=("lead_owner"))
    # print(abc)
    if (('CRM User' in frappe.get_roles(user) or 'Partner User' in frappe.get_roles(user))  and not 'Sales User' in frappe.get_roles(user) and not 'Sales Manager' in frappe.get_roles(user) and doc.loan_amount != None and doc.location!= None and doc.product_required!= None):
        location = frappe.db.sql("""select location_name from `tabProduct Sales Team` where parent = %s""",doc.product_required)
        amount_threshold = frappe.db.sql("""select amount_threshold from `tabProduct Sales Team` where parent = %s and location_name = %s""", (doc.product_required, doc.location))
        print(location)
        print(amount_threshold)
        res4 = [element for tupl in location for element in tupl]
        print(res4)
        if doc.location not in res4:
            frappe.throw("Location Not found for this Product ")
        res6 = [element for tupl in amount_threshold for element in tupl]
        print(res6)
        res7 = max(res6)
        print(res7)
        # res8 = res7[-1]
        # print(res8)
        if doc.loan_amount > res7 or doc.loan_amount < 1:
            frappe.throw("Loan Amount not found for this Product")
        abc = frappe.db.get_list("Lead", filters={'workflow_state':('not in',('Amount Credited')),"lead_owner":sales_person[0][0]}, fields=("lead_owner"))
        print(abc)
        res = [d['lead_owner'] for d in abc]
        count = res.count(doc.lead_owner)
        lead_count1 = frappe.db.sql("""select leads_count from `tabSales Person` where name = %s""", (sales_person[0][0]))
        reporting_manager = frappe.db.sql("""select parent_sales_person from `tabSales Person` where name = %s""", (sales_person[0][0]))
        abc2 = frappe.db.get_list("Lead", filters={'workflow_state':('not in',('Amount Credited')),"lead_owner":reporting_manager[0][0]}, fields=("lead_owner"))
        res2 = [d['lead_owner'] for d in abc2]
        count2 = res2.count(reporting_manager[0][0])
        reporting_manager2 = frappe.db.sql("""select parent_sales_person from `tabSales Person` where name = %s""", (reporting_manager[0][0]))
        lead_count2 = frappe.db.sql("""select leads_count from `tabSales Person` where name = %s""", (reporting_manager[0][0]))
        abc3 = frappe.db.get_list("Lead", filters={'workflow_state':('not in',('Amount Credited')),"lead_owner":sales_person[0][0]}, fields=("lead_owner"))
        res3 = [d['lead_owner'] for d in abc3]
        count3 = res3.count(doc.lead_owner)     
        lead_count3 = frappe.db.sql("""select leads_count from `tabSales Person` where name = %s""", (sales_person[0][0]))
        reporting_manager = frappe.db.sql("""select parent_sales_person from `tabSales Person` where name = %s""", (sales_person[0][0]))
        print(location)
                

        if res.count(doc.lead_owner) <= int(lead_count1[0][0]):
            doc.lead_owner = sales_person[0][0]
            subject = frappe.db.get_value('User', {"name":doc.lead_owner}, 'mobile_no')
            doc.lead_owner_mobile_no = subject
        if count2 >= int(lead_count2[0][0]):
            frappe.msgprint("Already 15 Leads Assigned, So this lead is assigned to reporting manager")
            doc.lead_owner = reporting_manager2[0][0]
            subject = frappe.db.get_value('User', {"name":doc.lead_owner}, 'mobile_no')
            doc.lead_owner_mobile_no = subject
        if res3.count(doc.lead_owner) >= int(lead_count3[0][0]):
            frappe.msgprint("Already 15 Leads Assigned, So this lead is assigned to reporting manager")
            doc.lead_owner = reporting_manager[0][0]
            subject = frappe.db.get_value('User', {"name":doc.lead_owner}, 'mobile_no')
            doc.lead_owner_mobile_no = subject

        email = doc.lead_owner
        user_name = frappe.get_doc('User', email).full_name
        emailmessage = """Dear {},<br><br>
        Lead of {} with Lead ID {} has been allocated to you.<br>
        Kindly attend to the lead and update the status within 2 hours.<br><br>
        Best Regards,<br>
        CRM Team.""".format(user_name, doc.lead_name, doc.name)
        frappe.sendmail(subject="Lead Allocated", content=emailmessage, recipients = '{}'.format(doc.lead_owner),sender="mycrm@switchmyloan.in")


@frappe.whitelist()
def update_status(lead,status):
    doc = frappe.get_doc("Lead",lead)
    doc.set_status(update = True, status = status)
    doc.reload()






