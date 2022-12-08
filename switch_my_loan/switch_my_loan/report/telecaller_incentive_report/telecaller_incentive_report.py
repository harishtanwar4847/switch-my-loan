# Copyright (c) 2013, Atrina Technologies Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import itertools

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	columns = [
		{
			'fieldname': 'telecaller name',
			'label': _('Telecaller'),
			'fieldtype': 'Link',
			'options': 'User',
			'width':250
		},
		{
			'fieldname': 'total revenue',
			'label': _('Total Revenue'),
			'fieldtype': 'Currency',
			'options': 'Currency',
			'width':200
		},
		{
			'fieldname': 'telecaller incentive',
			'label': _('Telecaller Incentive'),
			'fieldtype': 'Currency',
			'options': 'currency',
			'width':200
		}
	]
	return columns

def get_data(filters):
	l1 = []
	l2 = []
	l3 = []
	l4 = []
	l5 = []
	telecaller_name = frappe.db.sql("""select distinct(telecaller_name) from `tabLead` where telecaller_name is not null and supplier_group is null and workflow_state = 'Amount Credited'""")
	for i in telecaller_name:
		l1.append(i[0])
		total_revenue = frappe.db.sql("""select SUM(l.total_revenue) from `tabLead` l where l.workflow_state = 'Amount Credited' and l.supplier_group is null and l.telecaller_name = %s and date(l.amount_credited_time) between %s and %s""",(i[0],filters.from_date,filters.to_date),)
		l2.append(total_revenue[0][0])
		salary = frappe.db.sql("""select employee_salary from `tabEmployee` e where e.user_id = %s""",(i[0]))
		if salary:
			l3.append(salary[0][0])
		else:
			l3.append(0)
	for i in l2:
		if i is not None:
			divisional_amount = i*50/100
			l4.append(divisional_amount)
		else:
			l4.append(0)

	amount_threshold = frappe.db.sql("""select from_amount,to_amount,percent from `tabEmployee Incentive Detail` where parent = 'Telecaller'""")
	
	for (i,j) in zip(l3,l4):
		if i*6 >= j:
			l5.append(0)
		else:
			eligible_divisional_amount = j - i*6
			for x in amount_threshold:
				if x[1] > 0:
					if eligible_divisional_amount >= x[0] and eligible_divisional_amount <= x[1]:
						telecaller_incentive = eligible_divisional_amount * x[2]/100
						l5.append(telecaller_incentive)
				if x[1] == 0:
					if eligible_divisional_amount >= x[0]:
						telecaller_incentive = eligible_divisional_amount * x[2]/100
						l5.append(telecaller_incentive)
			
	data = []
	row = []
	for (i,j,k) in zip(l1,l2,l5):
		row = [i,j,k]
		data.append(row)		
	return data