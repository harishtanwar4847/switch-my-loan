import frappe
from datetime import datetime
from frappe.utils import getdate
from datetime import date
from frappe.utils import date_diff
from jinja2 import Template

def unattended_leads_after_two_hours_at_twelve():
    su_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales User'""", as_list=1)]
    for i in range(len(su_list)):
        leadlist = frappe.db.get_list('Lead', fields=("name","lead_name","loan_amount","product_required","creation","lead_owner"),filters={"lead_owner":su_list[i],"workflow_state":"Open"}, as_list = True)
        print(leadlist)
        leadlist2 = []
        if leadlist:
            for lead in leadlist:
                print(lead[0])
                l = frappe.get_doc('Lead',lead[0])
                print(l)
                today = date.today()
                print(today)
                print(getdate(l.modified))
                diff = datetime.now() - l.modified
                print(diff)
                diff_in_hours = diff.total_seconds() / 3600
                print(diff_in_hours)
                if diff_in_hours >= 2 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            print(leadlist2)
            notification = frappe.get_doc('Notification', 'Leads Unattended From Last 2 Hours')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=su_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))

def unattended_leads_after_two_hours_at_two():
    su_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales User'""", as_list=1)]
    for i in range(len(su_list)):
        leadlist = frappe.db.get_list('Lead', fields=("name","lead_name","loan_amount","product_required","creation","lead_owner"),filters={"lead_owner":su_list[i],"workflow_state":"Open"}, as_list = True)
        print(leadlist)
        leadlist2 = []
        if leadlist:
            for lead in leadlist:
                print(lead[0])
                l = frappe.get_doc('Lead',lead[0])
                print(l)
                today = date.today()
                print(today)
                print(getdate(l.modified))
                diff = datetime.now() - l.modified
                print(diff)
                diff_in_hours = diff.total_seconds() / 3600
                print(diff_in_hours)
                if diff_in_hours >= 2 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            print(leadlist2)
            notification = frappe.get_doc('Notification', 'Leads Unattended From Last 2 Hours')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=su_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))

def unattended_leads_after_two_hours_at_four():
    su_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales User'""", as_list=1)]
    for i in range(len(su_list)):
        leadlist = frappe.db.get_list('Lead', fields=("name","lead_name","loan_amount","product_required","creation","lead_owner"),filters={"lead_owner":su_list[i],"workflow_state":"Open"}, as_list = True)
        print(leadlist)
        leadlist2 = []
        if leadlist:
            for lead in leadlist:
                print(lead[0])
                l = frappe.get_doc('Lead',lead[0])
                print(l)
                today = date.today()
                print(today)
                print(getdate(l.modified))
                diff = datetime.now() - l.modified
                print(diff)
                diff_in_hours = diff.total_seconds() / 3600
                print(diff_in_hours)
                if diff_in_hours >= 2 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            print(leadlist2)
            notification = frappe.get_doc('Notification', 'Leads Unattended From Last 2 Hours')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=su_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))

def unattended_leads_after_two_hours_at_six():
    su_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales User'""", as_list=1)]
    for i in range(len(su_list)):
        leadlist = frappe.db.get_list('Lead', fields=("name","lead_name","loan_amount","product_required","creation","lead_owner"),filters={"lead_owner":su_list[i],"workflow_state":"Open"}, as_list = True)
        print(leadlist)
        leadlist2 = []
        if leadlist:
            for lead in leadlist:
                print(lead[0])
                l = frappe.get_doc('Lead',lead[0])
                print(l)
                today = date.today()
                print(today)
                print(getdate(l.modified))
                diff = datetime.now() - l.modified
                print(diff)
                diff_in_hours = diff.total_seconds() / 3600
                print(diff_in_hours)
                if diff_in_hours >= 2 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            print(leadlist2)
            notification = frappe.get_doc('Notification', 'Leads Unattended From Last 2 Hours')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=su_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))


def unattended_leads_after_four_hours_at_two():
    su_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales User'""", as_list=1)]
    for i in range(len(su_list)):
        leadlist = frappe.db.get_list('Lead', fields=("name","lead_name","loan_amount","product_required","creation","lead_owner"),filters={"lead_owner":su_list[i],"workflow_state":"Open"}, as_list = True)
        print(leadlist)
        leadlist2 = []
        if leadlist:
            for lead in leadlist:
                print(lead[0])
                l = frappe.get_doc('Lead',lead[0])
                print(l)
                today = date.today()
                print(today)
                print(getdate(l.modified))
                diff = datetime.now() - l.modified
                print(diff)
                diff_in_hours = diff.total_seconds() / 3600
                print(diff_in_hours)
                if diff_in_hours >= 4 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            print(leadlist2)
            notification = frappe.get_doc('Notification', 'Leads Unattended From Last 4 Hours')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=su_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))

    sm_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales Manager'""", as_list=1)]
    for i in range(len(sm_list)):
        sm = frappe.db.sql("""select l.name,l.lead_name,l.loan_amount,l.product_required,l.creation,l.lead_owner from `tabLead` as l 
        join `tabSales Person` as sp 
        on sp.name = l.lead_owner   
        where l.workflow_state = "Open" and sp.parent_sales_person = %s""",(sm_list[i]))
        leadlist2 = []
        if sm:
            for lead in sm:
                l = frappe.get_doc('Lead',lead[0])
                today = date.today()
                diff = datetime.now() - l.modified
                diff_in_hours = diff.total_seconds() / 3600
                if diff_in_hours >= 4 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            notification = frappe.get_doc('Notification', 'Leads Unattended From Last 4 Hours')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=sm_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))

def unattended_leads_after_four_hours_at_six():
    su_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales User'""", as_list=1)]
    for i in range(len(su_list)):
        leadlist = frappe.db.get_list('Lead', fields=("name","lead_name","loan_amount","product_required","creation","lead_owner"),filters={"lead_owner":su_list[i],"workflow_state":"Open"}, as_list = True)
        print(leadlist)
        leadlist2 = []
        if leadlist:
            for lead in leadlist:
                print(lead[0])
                l = frappe.get_doc('Lead',lead[0])
                print(l)
                today = date.today()
                print(today)
                print(getdate(l.modified))
                diff = datetime.now() - l.modified
                print(diff)
                diff_in_hours = diff.total_seconds() / 3600
                print(diff_in_hours)
                if diff_in_hours >= 4 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            print(leadlist2)
            notification = frappe.get_doc('Notification', 'Leads Unattended From Last 4 Hours')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=su_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))

    sm_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales Manager'""", as_list=1)]
    for i in range(len(sm_list)):
        sm = frappe.db.sql("""select l.name,l.lead_name,l.loan_amount,l.product_required,l.creation,l.lead_owner from `tabLead` as l 
        join `tabSales Person` as sp 
        on sp.name = l.lead_owner   
        where l.workflow_state = "Open" and sp.parent_sales_person = %s""",(sm_list[i]))
        leadlist2 = []
        if sm:
            for lead in sm:
                l = frappe.get_doc('Lead',lead[0])
                today = date.today()
                diff = datetime.now() - l.modified
                diff_in_hours = diff.total_seconds() / 3600
                if diff_in_hours >= 4 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            notification = frappe.get_doc('Notification', 'Leads Unattended From Last 4 Hours')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=sm_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))


def unattended_leads_daily_at_ten():
    su_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales User'""", as_list=1)]
    for i in range(len(su_list)):
        leadlist = frappe.db.get_list('Lead', fields=("name","lead_name","loan_amount","product_required","creation","lead_owner"),filters={"lead_owner":su_list[i],"workflow_state":"Open"}, as_list = True)
        print(leadlist)
        leadlist2 = []
        if leadlist:
            for lead in leadlist:
                print(lead[0])
                l = frappe.get_doc('Lead',lead[0])
                print(l)
                today = date.today()
                print(today)
                print(getdate(l.modified))
                diff = datetime.now() - l.modified
                print(diff)
                diff_in_hours = diff.total_seconds() / 3600
                print(diff_in_hours)
                if diff_in_hours >= 24 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            print(leadlist2)
            notification = frappe.get_doc('Notification', 'Leads Unattended Yesterday')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=su_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))
    
    sm_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales Manager'""", as_list=1)]
    for i in range(len(sm_list)):
        sm = frappe.db.sql("""select l.name,l.lead_name,l.loan_amount,l.product_required,l.creation,l.lead_owner from `tabLead` as l 
        join `tabSales Person` as sp 
        on sp.name = l.lead_owner   
        where l.workflow_state = "Open" and sp.parent_sales_person = %s""",(sm_list[i]))
        leadlist2 = []
        if sm:
            for lead in sm:
                l = frappe.get_doc('Lead',lead[0])
                today = date.today()
                diff = datetime.now() - l.modified
                diff_in_hours = diff.total_seconds() / 3600
                if diff_in_hours >= 24 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            notification = frappe.get_doc('Notification', 'Leads Unattended Yesterday')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=sm_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))
    
    exco_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Exco'""", as_list=1)]
    for i in range(len(exco_list)):
        leadlist = frappe.db.get_list('Lead', fields=("name","lead_name","loan_amount","product_required","creation","lead_owner"),filters={"workflow_state":"Open"}, as_list = True)
        print(leadlist)
        leadlist2 = []
        if leadlist:
            for lead in leadlist:
                print(lead[0])
                l = frappe.get_doc('Lead',lead[0])
                print(l)
                today = date.today()
                print(today)
                print(getdate(l.modified))
                diff = datetime.now() - l.modified
                print(diff)
                diff_in_hours = diff.total_seconds() / 3600
                print(diff_in_hours)
                if diff_in_hours >= 24 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            print(leadlist2)
            notification = frappe.get_doc('Notification', 'Leads Unattended Yesterday')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=exco_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))
    
def unattended_leads_daily_at_seven():
    su_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales User'""", as_list=1)]
    for i in range(len(su_list)):
        leadlist = frappe.db.get_list('Lead', fields=("name","lead_name","loan_amount","product_required","creation","lead_owner"),filters={"lead_owner":su_list[i],"workflow_state":"Open"}, as_list = True)
        print(leadlist)
        leadlist2 = []
        if leadlist:
            for lead in leadlist:
                print(lead[0])
                l = frappe.get_doc('Lead',lead[0])
                print(l)
                today = date.today()
                print(today)
                print(getdate(l.modified))
                diff = datetime.now() - l.modified
                print(diff)
                diff_in_hours = diff.total_seconds() / 3600
                print(diff_in_hours)
                if diff_in_hours >= 24 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            print(leadlist2)
            notification = frappe.get_doc('Notification', 'Leads Unattended Yesterday')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=su_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))
    
    sm_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales Manager'""", as_list=1)]
    for i in range(len(sm_list)):
        sm = frappe.db.sql("""select l.name,l.lead_name,l.loan_amount,l.product_required,l.creation,l.lead_owner from `tabLead` as l 
        join `tabSales Person` as sp 
        on sp.name = l.lead_owner   
        where l.workflow_state = "Open" and sp.parent_sales_person = %s""",(sm_list[i]))
        leadlist2 = []
        if sm:
            for lead in sm:
                l = frappe.get_doc('Lead',lead[0])
                today = date.today()
                diff = datetime.now() - l.modified
                diff_in_hours = diff.total_seconds() / 3600
                if diff_in_hours >= 24 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            notification = frappe.get_doc('Notification', 'Leads Unattended Yesterday')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=sm_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))
    
    exco_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Exco'""", as_list=1)]
    for i in range(len(exco_list)):
        leadlist = frappe.db.get_list('Lead', fields=("name","lead_name","loan_amount","product_required","creation","lead_owner"),filters={"workflow_state":"Open"}, as_list = True)
        print(leadlist)
        leadlist2 = []
        if leadlist:
            for lead in leadlist:
                print(lead[0])
                l = frappe.get_doc('Lead',lead[0])
                print(l)
                today = date.today()
                print(today)
                print(getdate(l.modified))
                diff = datetime.now() - l.modified
                print(diff)
                diff_in_hours = diff.total_seconds() / 3600
                print(diff_in_hours)
                if diff_in_hours >= 24 and l.workflow_state != "Amount Credited" and l.status != "On Hold" and l.status != "Rejected" and l.status != "Drop":
                    leadlist2.append(lead)
            print(leadlist2)
            notification = frappe.get_doc('Notification', 'Leads Unattended Yesterday')
            l.leads = leadlist2
            args={'doc': l}
            recipients,cc,bb = notification.get_list_of_recipients(l, args)
            frappe.enqueue(method=frappe.sendmail, recipients=exco_list[i], sender=None, 
            subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))
    