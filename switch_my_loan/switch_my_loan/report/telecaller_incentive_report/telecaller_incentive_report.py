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
	print(telecaller_name)
	for i in telecaller_name:
		print(i[0])
		l1.append(i[0])
		total_revenue = frappe.db.sql("""select SUM(l.total_revenue) from `tabLead` l where l.workflow_state = 'Amount Credited' and l.supplier_group is null and l.telecaller_name = %s and date(l.creation) between %s and %s""",(i[0],filters.from_date,filters.to_date),)
		print(total_revenue)
		l2.append(total_revenue[0][0])
		salary = frappe.db.sql("""select employee_salary from `tabEmployee` e where e.user_id = %s""",(i[0]))
		print(salary)
		if salary:
			l3.append(salary[0][0])
		else:
			l3.append(0)
	for i in l2:
		print(i)
		if i is not None:
			divisional_amount = i*50/100
			print(divisional_amount)
			l4.append(divisional_amount)
		else:
			l4.append(0)

	print("====================")
	print("====Incentive Details")
	amount_threshold = frappe.db.sql("""select from_amount,to_amount,percent from `tabEmployee Incentive Detail` where parent = 'Telecaller'""")
	# percent = frappe.db.sql("""select to_amount from `tabEmployee Incentive Detail` where parent = 'Telecaller' and to_amount = %s""")
	# for i in amount_threshold:
	# 	percent = frappe.db.sql("""select percent from `tabEmployee Incentive Detail` where parent = 'Telecaller' and to_amount = %s""",(i[0]))
	# 	print(percent)
	print(amount_threshold)
	

	print("===========")
	print("Incentive")
	for (i,j) in zip(l3,l4):
		if i*6 >= j:
			l5.append(0)
		else:
			eligible_divisional_amount = j - i*6
			for i in amount_threshold:
				if i[1] > 0:
					if eligible_divisional_amount >= i[0] and eligible_divisional_amount <= i[1]:
						telecaller_incentive = eligible_divisional_amount * i[2]/100
				if i[1] == 0:
					if eligible_divisional_amount >= i[0]:
						telecaller_incentive = eligible_divisional_amount * i[2]/100
			# elif eligible_divisional_amount > 100000 and eligible_divisional_amount < 250000:
			# 	telecaller_incentive = eligible_divisional_amount * 12.5/100
			# elif eligible_divisional_amount > 250000 and eligible_divisional_amount < 500000:
			# 	telecaller_incentive = eligible_divisional_amount * 15/100
			# elif eligible_divisional_amount > 500000:
			# 	telecaller_incentive = eligible_divisional_amount * 17.5/100
					l5.append(telecaller_incentive)

	print(l1)
	print(l2)
	print(l3)
	print(l4)
	print(l5)
	data = []
	row = []
	for (i,j,k) in zip(l1,l2,l5):
		row = [i,j,k]
		data.append(row)		
	return data