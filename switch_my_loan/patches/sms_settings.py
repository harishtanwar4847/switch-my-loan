from __future__ import unicode_literals
import frappe

def execute():
    doc = frappe.get_doc('SMS Settings')
    doc.sms_gateway_url = "http://bulkpush.mytoday.com/BulkSms/SingleMsgApi"
    doc.message_parameter = "Text"
    doc.receiver_parameter = "To"
    doc.append('parameters', {
        'parameter':'username',
        'value':'9920706289'
    })
    doc.append('parameters', {
        'parameter':'password',
        'value':'SwitchMyLoan@123'
    })
    doc.append('parameters', {
        'parameter':'feedid',
        'value':'385302'
    })
    doc.append('parameters', {
        'parameter':'aysnc',
        'value':'0'
    })
    doc.append('parameters', {
        'parameter':'short',
        'value':'0'
    })
    doc.append('parameters', {
        'parameter':'senderid',
        'value':'SMLBUD'
    })
    
    doc.save()
    frappe.db.commit()