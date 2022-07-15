# Copyright (c) 2013, Atrina Technologies Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from operator import le
from syslog import LOG_LOCAL6, LOG_LOCAL7
import frappe
from frappe import _
import itertools
from collections import defaultdict

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	columns = [
		{
			'fieldname': 'sales_person',
			'label': _('Sales Person'),
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
			'fieldname': 'sales person incentive',
			'label': _('Sales Person Incentive'),
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
	l6 = []
	l7 = []
	l8 = []
	l9 = []
	l10 = []
	l11 = []
	l12 = []
	l13 = []
	l14 = []
	l15 = []
	l16 = []
	l17 = []
	l18 = []
	l19 = []
	l20 = []
	l21 = []
	l22 = []
	l23 = []
	l24 = []
	l25 = []
	l26 = []
	l27 = []
	l28 = []
	l29 = []
	l30 = []
	l31 = []
	l32 = []
	l33 = []
	l34 = []
	l35 = []
	l36 = []
	l37 = []
	l38 = []
	l39 = []
	l40 = []
	l41 = []
	l42 = []
	l43 = []
	l44 = []
	l45 = []
	l46 = []
	l47 = []
	print("Fixed Cost =====================================================================")
	sales_person_name_fixed_cost = frappe.db.sql("""select lead_owner from `tabLead` where workflow_state = 'Amount Credited' and supplier_group = 'Fixed Cost' and creation between %s and %s""",(filters.from_date,filters.to_date),)
	print(sales_person_name_fixed_cost)
	for i in sales_person_name_fixed_cost:
		print(i)
		l1.append(i)
		salary = frappe.db.sql("""select employee_salary from `tabEmployee` e where e.user_id = %s""",(i[0]))
		print(salary)
		if salary:
			l2.append((i[0],salary[0][0]))
		else:
			l2.append((i[0],0.0))
		total_revenue_fixed_cost = frappe.db.sql("""select SUM(l.total_revenue) from `tabLead` l where l.workflow_state = 'Amount Credited' and l.supplier_group = 'Fixed Cost' and l.lead_owner = %s and creation between %s and %s""",(i[0],filters.from_date,filters.to_date),)
		print('----')
		print(total_revenue_fixed_cost)
		print('----')
		l3.append((i[0],total_revenue_fixed_cost[0][0]))

	for i in l3:
		l4.append((i[0],i[1]*0.5))

	for i in l2:
		if i not in l5:
			l5.append(i)

	for i in l3:
		if i not in l6:
			l6.append(i)

	for i in l4:
		if i not in l7:
			l7.append(i)

	print(l1)
	print(l2)
	print(l3)
	print(l4)

	print("=======================")
	print(l5)
	print(l6)
	print(l7)





	print("Null =====================================================================")
	sales_person_name_null = frappe.db.sql("""select lead_owner from `tabLead` where workflow_state = 'Amount Credited' and supplier_group is null and creation between %s and %s""",(filters.from_date,filters.to_date),)
	print(sales_person_name_null)
	for i in sales_person_name_null:
		print(i)
		l11.append(i)
		salary = frappe.db.sql("""select employee_salary from `tabEmployee` e where e.user_id = %s""",(i[0]))
		print(salary)
		if salary:
			l12.append((i[0],salary[0][0]))
		else:
			l12.append((i[0],0.0))
		total_revenue_null = frappe.db.sql("""select SUM(l.total_revenue) from `tabLead` l where l.workflow_state = 'Amount Credited' and l.supplier_group is null and l.lead_owner = %s and creation between %s and %s""",(i[0],filters.from_date,filters.to_date),)
		print('----')
		print(total_revenue_null)
		print('----')
		l13.append((i[0],total_revenue_null[0][0]))

	for i in l13:
		l14.append((i[0],i[1]*0.5)) 

	for i in l12:
		if i not in l15:
			l15.append(i)

	for i in l13:
		if i not in l16:
			l16.append(i)

	for i in l14:
		if i not in l17:
			l17.append(i)

	print(l11)
	print(l12)
	print(l13)
	print(l14)

	print("====================")
	print(l15)
	print(l16)
	print(l17)

	print("Fixed Commission =====================================================================")
	sales_person_name_fixed_commission = frappe.db.sql("""select lead_owner from `tabLead` where workflow_state = 'Amount Credited' and supplier_group = 'Fixed Commission' and creation between %s and %s""",(filters.from_date,filters.to_date),)
	print(sales_person_name_fixed_commission)
	for i in sales_person_name_fixed_commission:
		print(i)
		l21.append(i)
		salary = frappe.db.sql("""select employee_salary from `tabEmployee` e where e.user_id = %s""",(i[0]))
		print(salary)
		if salary:
			l22.append((i[0],salary[0][0]))
		else:
			l22.append((i[0],0.0))
		total_revenue_fixed_commission = frappe.db.sql("""select SUM(l.total_revenue) from `tabLead` l where l.workflow_state = 'Amount Credited' and l.supplier_group = 'Fixed Commission' and l.lead_owner = %s and creation between %s and %s""",(i[0],filters.from_date,filters.to_date),)
		print('----')
		print(total_revenue_fixed_commission)
		print('----')
		l23.append((i[0],total_revenue_fixed_commission[0][0]))

		lead_name = frappe.db.sql("""select lead_owner,name from `tabLead` where workflow_state = 'Amount Credited' and supplier_group = 'Fixed Commission' and lead_owner = %s and creation between %s and %s""",(i[0],filters.from_date,filters.to_date),)
		print(lead_name)
		for j in lead_name:			
			fixed_commission = frappe.db.sql("""select l.lead_owner,l.commission_rate,l.name from `tabLead` l where l.workflow_state = 'Amount Credited' and supplier_group = 'Fixed Commission' and l.lead_owner = %s and l.name=%s and l.creation between %s and %s""",(i[0],j[1], filters.from_date,filters.to_date),)
			l24.append(fixed_commission[0])

			total_revenue_fixed_commission = frappe.db.sql("""select l.lead_owner,l.total_revenue,l.name from `tabLead` l where l.workflow_state = 'Amount Credited' and l.lead_owner = %s and l.name=%s and creation between %s and %s""",(i[0],j[1],filters.from_date,filters.to_date),)
			print('----')
			print(total_revenue_fixed_commission)
			print('----')
			l25.append(total_revenue_fixed_commission[0])

	
	for i in l24:
		if i not in l26:
			l26.append(i)

	for i in l25:
		if i not in l27:
			l27.append(i)

	for (i,j) in zip(l26,l27):
		l28.append((i[0],j[1]*i[1]/100))


	for i in l22:
		if i not in l29:
			l29.append(i)

	for i in l23:
		if i not in l30:
			l30.append(i)

	l31 = defaultdict(float)
	for i,j in l28:
		l31[i] += float(j)

	for i,j in l31.items():
		l32.append((i,j))

	for (i,j) in zip(l30,l32):
		l33.append((i[0],i[1]-j[1]))

	
	print(l21)
	print(l22)
	print(l23)
	print(l24)
	print(l25)
	print(l26)
	print(l27)
	print(l28)

	print("=================================================")
	print(l29)
	print(l30)
	# print(l32)
	print(l33)

			

	print("======================")
	print("Incentive Details")
	amount_threshold = frappe.db.sql("""select from_amount,to_amount,percent from `tabEmployee Incentive Detail` where parent = 'Sales User'""")
	# percent = frappe.db.sql("""select to_amount from `tabEmployee Incentive Detail` where parent = 'Telecaller' and to_amount = %s""")
	# for i in amount_threshold:
	# 	percent = frappe.db.sql("""select percent from `tabEmployee Incentive Detail` where parent = 'Telecaller' and to_amount = %s""",(i[0]))
	# 	print(percent)
	print(amount_threshold)
	
	
	print("===========================")
	print("Incentive")
	for (i,j) in zip(l5,l7):
		if i[1]*6 >= j[1]:
			l34.append((i[0],0.0))
		else:
			eligible_divisional_amount = j[1] - i[1]*6			
			for x in amount_threshold:
				if x[1] > 0:
					if eligible_divisional_amount >= x[0] and eligible_divisional_amount <= x[1]:
						sale_person_incentive_a = eligible_divisional_amount * x[2]/100
						l34.append((i[0],sale_person_incentive_a))
				if x[1] == 0:
					if eligible_divisional_amount >= x[0]:
						sale_person_incentive_a = eligible_divisional_amount * x[2]/100
						l34.append((i[0],sale_person_incentive_a))
					
	print("Fixed Cost")
	print(l34)
	for (i,j) in zip(l15,l17):
		if i[1]*6 >= j[1]:
			l35.append((i[0],0.0))
		else:
			eligible_divisional_amount = j[1] - i[1]*6
			for x in amount_threshold:
				if x[1] > 0:
					if eligible_divisional_amount >= x[0] and eligible_divisional_amount <= x[1]:
						sale_person_incentive_b = eligible_divisional_amount * x[2]/100
						l35.append((i[0],sale_person_incentive_b))

				if x[1] == 0:
					if eligible_divisional_amount >= x[0]:
						sale_person_incentive_b = eligible_divisional_amount * x[2]/100
						l35.append((i[0],sale_person_incentive_b))
	
	print("Null")
	print(l35)
	for (i,j) in zip(l29,l33):
		if i[1]*6 >= j[1]:
			l36.append((i[0],0.0))
		else:
			eligible_divisional_amount = j[1] - i[1]*6
			for x in amount_threshold:
				if x[1] > 0:
					if eligible_divisional_amount >= x[0] and eligible_divisional_amount <= x[1]:
						sale_person_incentive_c = eligible_divisional_amount * x[2]/100
						l36.append((i[0],sale_person_incentive_c))

				if x[1] == 0:
					if eligible_divisional_amount >= x[0]:
						sale_person_incentive_c = eligible_divisional_amount * x[2]/100
						l36.append((i[0],sale_person_incentive_c))
				
	
	print("Fixed Commission")
	print(l36)

	l37 = l34+l35+l36
	l38 = defaultdict(float)
	for i,j in l37:
		l38[i] += float(j)

	for i,j in l38.items():
		l39.append((i,j))

	l42 = l6+l16+l30
	l43 = defaultdict(float)
	for i,j in l42:
		l43[i] += float(j)

	for i,j in l43.items():
		l44.append((i,j))

	print("Total Revenue")
	print(l42)
	print(l43)
	print(l44)

	for i in l44:
		l45.append(i[1])

	print(l45)



	print("sales Incentive")
	print(l37)
	print(l38)
	print(l39)

	for i in l39:
		l40.append(i[0])

	for i in l39:
		l41.append(i[1])

	print(l40)
	print(l41)
	# # print(l16)
	# # print(l17)

	data = []
	row = []
	for (i,j,k) in zip(l40,l45,l41):
		row = [i,j,k]
		data.append(row)		
	return data
