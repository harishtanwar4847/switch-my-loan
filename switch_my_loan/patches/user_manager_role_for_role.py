from __future__ import unicode_literals
import frappe
from frappe.permissions import (reset_perms, get_linked_doctypes, get_all_perms,setup_custom_perms, add_permission, update_permission_property)

def execute():
    add_permission(doctype ="Role", role = "User Manager", permlevel = 0, ptype=None)
    add_permission(doctype ="User", role = "User Manager", permlevel = 0, ptype=None)
    add_permission(doctype ="User", role = "User Manager", permlevel = 1, ptype=None)
    ptypes = ["read","write","create","report","print","email"]
    ptypes1= ["read","write","create","delete","report","import","print","email","share","export","set_user_permissions"]
    ptypes2 = ["read","write","export"]
    for ptype in ptypes:
        update(doctype = "Role", role = "User Manager", permlevel = 0, ptype = ptype, value=1)
    for ptype in ptypes1:
        update(doctype = "User", role = "User Manager", permlevel = 0, ptype = ptype, value=1)
    for ptype in ptypes2 :
        update(doctype = "User", role = "User Manager", permlevel = 1, ptype = ptype, value=1)


def copy_perms(parent):
	'''Copy all DocPerm in to Custom DocPerm for the given document'''
	for d in frappe.get_all('DocPerm', fields='*', filters=dict(parent=parent)):
		custom_perm = frappe.new_doc('Custom DocPerm')
		custom_perm.update(d)
		custom_perm.insert(ignore_permissions=True)

def setup_custom_perms(parent):
	'''if custom permssions are not setup for the current doctype, set them up'''
	if not frappe.db.exists('Custom DocPerm', dict(parent=parent)):
		copy_perms(parent)
		return True



def add_permission(doctype, role, permlevel=0, ptype=None):
	'''Add a new permission rule to the given doctype
		for the given Role and Permission Level'''
	from frappe.core.doctype.doctype.doctype import validate_permissions_for_doctype
	setup_custom_perms(doctype)

	if frappe.db.get_value('Custom DocPerm', dict(parent=doctype, role=role,
		permlevel=permlevel, if_owner=0)):
		return

	if not ptype:
		ptype = 'read'

	custom_docperm = frappe.get_doc({
		"doctype":"Custom DocPerm",
		"__islocal": 1,
		"parent": doctype,
		"parenttype": "DocType",
		"parentfield": "permissions",
		"role": role,
		"permlevel": permlevel,
		ptype: 1,
	})

	custom_docperm.save()

	validate_permissions_for_doctype(doctype)
	return custom_docperm.name

def update_permission_property(doctype, role, permlevel, ptype, value=None, validate=True):
	'''Update a property in Custom Perm'''
	from frappe.core.doctype.doctype.doctype import validate_permissions_for_doctype
	out = setup_custom_perms(doctype)

	name = frappe.get_value('Custom DocPerm', dict(parent=doctype, role=role,
		permlevel=permlevel))

	frappe.db.sql("""
		update `tabCustom DocPerm`
		set `{0}`=%s where name=%s""".format(ptype), (value, name))
	if validate:
		validate_permissions_for_doctype(doctype)

	return out

def update(doctype, role, permlevel, ptype, value=None):
	print(doctype)
	print(role)
	print(permlevel)
	print(ptype)
	print(value)
	"""Update role permission params

	Args:
	    doctype (str): Name of the DocType to update params for
	    role (str): Role to be updated for, eg "Website Manager".
	    permlevel (int): perm level the provided rule applies to
	    ptype (str): permission type, example "read", "delete", etc.
	    value (None, optional): value for ptype, None indicates False

	Returns:
	    str: Refresh flag is permission is updated successfully
	"""
	frappe.only_for("System Manager")
	out = update_permission_property(doctype, role, permlevel, ptype, value)
	return 'refresh' if out else None


