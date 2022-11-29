# Copyright (c) 2013, Atrina Technologies Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from syslog import LOG_LOCAL7
import frappe
from frappe import _
import itertools

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	columns = [
		{
			'fieldname': 'sourcing agent',
			'label': _('Sourcing Agent'),
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
			'fieldname': 'supplier payout',
			'label': _('Supplier Payout'),
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
	sourcing_agent_fixed_cost = frappe.db.sql("""select distinct(l.sourcing_agent) from `tabLead` l where l.supplier_group = 'Fixed Cost'""")
	for i in sourcing_agent_fixed_cost:
		l1.append(i[0])
		total_revenue_fixed_cost = frappe.db.sql("""select SUM(l.total_revenue) from `tabLead` l where l.workflow_state = 'Amount Credited' and l.supplier_group = 'Fixed Cost' and l.sourcing_agent = %s and date(l.amount_credited_time) between %s and %s""",(i[0],filters.from_date,filters.to_date),)
		if total_revenue_fixed_cost[0][0] is not None:
			l2.append(total_revenue_fixed_cost[0][0])
		else:
			l2.append(0)
		
		fixed_cost = frappe.db.sql("""select l.fixed_cost from `tabLead` l where l.supplier_group = 'Fixed Cost' and l.sourcing_agent = %s""",(i[0]))
		if fixed_cost is not None:
			l3.append(fixed_cost[0][0])
		else:
			l3.append(0)

		commission_rate = frappe.db.sql("""select l.commission_rate from `tabLead` l where l.supplier_group = 'Fixed Cost' and l.sourcing_agent = %s""",(i[0]))
		if commission_rate is not None:
			l4.append(commission_rate[0][0])
		else:
			l4.append(0)

	sourcing_agent_fixed_commission = frappe.db.sql("""select distinct(l.sourcing_agent) from `tabLead` l where l.supplier_group = 'Fixed Commission'""")
	for i in sourcing_agent_fixed_commission:
		l5.append(i[0])
		total_revenue_fixed_commission = frappe.db.sql("""select SUM(l.total_revenue) from `tabLead` l where l.workflow_state = 'Amount Credited' and l.supplier_group = 'Fixed Commission' and l.sourcing_agent = %s and date(l.amount_credited_time) between %s and %s""",(i[0],filters.from_date,filters.to_date),)
		if total_revenue_fixed_commission[0][0] is not None:
			l6.append(total_revenue_fixed_commission[0][0])
		else:
			l6.append(0)

		commission_rate = frappe.db.sql("""select l.commission_rate from `tabLead` l where l.supplier_group = 'Fixed Commission' and l.sourcing_agent = %s""",(i[0]))
		if commission_rate is not None:
			l7.append(commission_rate[0][0])
		else:
			l7.append(0)
		


	for (i,j,k) in zip(l2,l3,l4):
		supplier_payout = j + ((i-j)*k/100)
		if supplier_payout > 0:
			l8.append(supplier_payout)
		else:
			l8.append(0)

	for (i,j) in zip(l6,l7):
		supplier_payout = i*j/100
		if supplier_payout > 0:
			l9.append(supplier_payout)
		else:
			l9.append(0)

	l1 = l1 + l5
	l2 = l2 + l6
	l3 = l3 + l6
	l4 = l4 + l7
	l8 = l8 + l9
	data = []
	row = []
	for (i,j,k) in zip(l1,l2,l8):
		row = [i,j,k]
		data.append(row)		
	return data