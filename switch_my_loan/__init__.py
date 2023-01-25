__version__ = '1.2.1'

import frappe
import os
import json

@frappe.whitelist()
def neodove_webhook():
    log_file_path = frappe.utils.get_files_path('neodove.json')

    logs = "[]" 
    if os.path.exists(log_file_path):
        with open(log_file_path, "r") as f:
            logs = f.read()
        f.close()
    
    logs = json.loads(logs)
    logs.append(frappe.local.form_dict)
    with open(log_file_path, "w") as f:
        f.write(json.dumps(logs))
    f.close()
    
    frappe.response.message = frappe.form_dict

# modifying frappe.core.doctype.sms_settings.sms_settings.send_sms as send_sms_custom to take sms_template_id input
from frappe.core.doctype.sms_settings.sms_settings import validate_receiver_nos, send_via_gateway
from six import string_types
from frappe.modules.utils import get_doc_module
from frappe.utils import is_html

def send_sms_custom(receiver_list, msg, sender_name = '', success_msg = True, sms_template_id=None):
	import json
	if isinstance(receiver_list, string_types):
		receiver_list = json.loads(receiver_list)
		if not isinstance(receiver_list, list):
			receiver_list = [receiver_list]

	receiver_list = validate_receiver_nos(receiver_list)

	arg = {
		'receiver_list' : receiver_list,
		'message'		: frappe.safe_decode(msg).encode('utf-8'),
		'success_msg'	: success_msg,
		'sms_template_id': sms_template_id
	}

	if frappe.db.get_value('SMS Settings', None, 'sms_gateway_url'):
		send_via_gateway_custom(arg)
	else:
		frappe.msgprint(frappe._("Please Update SMS Settings"))

# monkey patch for frappe.email.doctype.notification.notification.Notification.send_sms to use send_sms_custom instead of send_sms 
# and passing notification.sms_template_id in the send_sms_custom method
def send_sms_notif(self, doc, context):
	send_sms_custom(
		receiver_list=self.get_receiver_list(doc, context),
		msg=frappe.render_template(self.message, context),
		sms_template_id=context['alert'].sms_template_id
	)

from frappe.email.doctype.notification.notification import Notification
Notification.send_sms = send_sms_notif

# monkey patch for frappe.core.doctype.sms_settings.sms_settings.send_via_gateway to inject templateid in args
from frappe.core.doctype.sms_settings.sms_settings import get_headers, send_request, create_sms_log
def send_via_gateway_custom(arg):
	ss = frappe.get_doc('SMS Settings', 'SMS Settings')
	headers = get_headers(ss)
	use_json = headers.get("Content-Type") == "application/json"

	message = frappe.safe_decode(arg.get('message'))
	args = {ss.message_parameter: message}
	for d in ss.get("parameters"):
		if not d.header:
			args[d.parameter] = d.value

	if arg['sms_template_id']:
		args['templateid'] = arg['sms_template_id']

	success_list = []
	for d in arg.get('receiver_list'):
		args[ss.receiver_parameter] = d
		status = send_request(ss.sms_gateway_url, args, headers, ss.use_post, use_json)

		if 200 <= status < 300:
			success_list.append(d)

	if len(success_list) > 0:
		args.update(arg)
		create_sms_log(args, success_list)
		if arg.get('success_msg'):
			frappe.msgprint(frappe._("SMS sent to following numbers: {0}").format("\n" + "\n".join(success_list)))
# frappe.core.doctype.sms_settings.sms_settings.send_via_gateway = send_via_gateway_custom

def load_standard_properties_custom(self, context):
    '''load templates and run get_context'''
    module = get_doc_module(self.module, self.doctype, self.name)
    if module:
        if hasattr(module, 'get_context'):
            out = module.get_context(context)
            if out: context.update(out)

    self.message = self.get_template()

    if self.channel != 'SMS':
        if not is_html(self.message):
            self.message = frappe.utils.md_to_html(self.message)

Notification.load_standard_properties = load_standard_properties_custom
