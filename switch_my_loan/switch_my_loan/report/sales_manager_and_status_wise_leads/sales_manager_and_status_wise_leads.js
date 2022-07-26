frappe.query_reports["Sales Manager and status wise Leads"] = {
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
