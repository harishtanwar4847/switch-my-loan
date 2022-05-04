import frappe
from datetime import datetime
from frappe.utils import getdate
from datetime import date
from frappe.utils import date_diff
from jinja2 import Template

def unattended_leads_hourly():
    leadlist = frappe.db.get_list('Lead', fields=("name","lead_name","loan_amount","product_required","creation","source"), as_list = True)
    print(leadlist)
    sm_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales Manager'""", as_list=1)]
    leadlist2 = []
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
        if diff_in_hours >= 2 and l.workflow_state != "Approved":
            leadlist2.append(lead)
    print(leadlist2)
    for i in range(len(sm_list)):
        notification = frappe.get_doc('Notification', 'Leads Unattended From Last 2 Hours')
        l.leads = leadlist2
        args={'doc': l}
        recipients,cc,bb = notification.get_list_of_recipients(l, args)
        frappe.enqueue(method=frappe.sendmail, recipients=sm_list[i], sender=None, 
        subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))

def unattended_leads_daily():
    leadlist = frappe.db.get_list('Lead', fields=("name","lead_name","loan_amount","product_required","creation","source"), as_list = True)
    print(leadlist)
    sm_list =[x[0] for x in frappe.db.sql("""select u.name from `tabUser` u inner join `tabHas Role` hr on hr.parent = u.name where hr.role = 'Sales Manager'""", as_list=1)]
    leadlist2 = []
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
        if diff_in_hours >= 24 and l.workflow_state != "Approved":
            leadlist2.append(lead)
    print(leadlist2)
    for i in range(len(sm_list)):
        notification = frappe.get_doc('Notification', 'Leads Unattended Yesterday')
        l.leads = leadlist2
        args={'doc': l}
        recipients,cc,bb = notification.get_list_of_recipients(l, args)
        frappe.enqueue(method=frappe.sendmail, recipients=sm_list[i], sender=None, 
        subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))

        
    