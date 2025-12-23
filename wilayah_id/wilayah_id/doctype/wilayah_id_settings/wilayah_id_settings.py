# Copyright (c) 2025, Jufer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from wilayah_id.setup.install import after_app_install

class WilayahIDSettings(Document):
    pass

@frappe.whitelist()
def reset():
	list_doctypes = ["Provinsi", "Kabupaten Atau Kota", "Kecamatan", "Desa Atau Kelurahan"]
	for doc_type in list_doctypes:
		frappe.db.truncate(doc_type)
	after_app_install()