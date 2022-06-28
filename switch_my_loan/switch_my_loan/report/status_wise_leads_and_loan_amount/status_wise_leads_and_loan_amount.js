frappe.query_reports["Status-wise Leads and Loan Amount"] = {
    "filters": [
         {
            "fieldname":"from_date",
            "label":("From Date"),
            "fieldtype":"Date",
            "default":frappe.datetime.month_start()
        },
         {
            "fieldname":"to_date",
            "label":("To Date"),
            "fieldtype":"Date",
            "default":frappe.datetime.month_end()
        },
]
}
