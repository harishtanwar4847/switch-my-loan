from . import __version__ as app_version

app_name = "switch_my_loan"
app_title = "Switch My Loan"
app_publisher = "Atrina Technologies Pvt Ltd"
app_description = "Switch My Loan"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@atriina.com"
app_license = "MIT"
app_logo_url = "/assets/switch_my_loan/images/switch_my_loan.jpeg"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/switch_my_loan/css/switch_my_loan.css"
# app_include_js = "/assets/switch_my_loan/js/switch_my_loan.js"

# include js, css files in header of web template
# web_include_css = "/assets/switch_my_loan/css/switch_my_loan.css"
# web_include_js = "/assets/switch_my_loan/js/switch_my_loan.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "switch_my_loan/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Lead" : "public/js/lead.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "switch_my_loan.install.before_install"
after_install = "switch_my_loan.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "switch_my_loan.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
    "Lead": "switch_my_loan.permissions.lead_query"
}
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
	"Lead":{
		"before_save":"switch_my_loan.utils.workflow_states",
        #"on_update":"switch_my_loan.utils.lead_owner",

	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"switch_my_loan.tasks.all"
# 	],
# 	"daily": [
# 		"switch_my_loan.tasks.daily"
# 	],
# 	"hourly": [
# 		"switch_my_loan.tasks.hourly"
# 	],
# 	"weekly": [
# 		"switch_my_loan.tasks.weekly"
# 	]
# 	"monthly": [
# 		"switch_my_loan.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "switch_my_loan.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "switch_my_loan.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "switch_my_loan.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"switch_my_loan.auth.validate"
# ]

