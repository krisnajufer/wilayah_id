import frappe
import json
import os

def after_app_install():
    import_provinsi()
    import_kabupaten_kota()
    import_kecamatan()
    import_kelurahan()

def import_provinsi():
    DOCTYPE = "Provinsi"

    file_path = os.path.join(
        frappe.get_app_path("wilayah_id"),
        "json",
        "provinsi.json"
    )

    if not os.path.exists(file_path):
        frappe.throw(f"Seed file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    fields = [
		"name",
        "provinsi",
        "zone_code"
	]
    for row in data:
        # CEGAH DUPLIKASI
        if frappe.db.exists(DOCTYPE, row.get("name")):
            continue

        rows.append(
            (
                row.get("name"),
                row.get("provinsi"),
                row.get("zone_code")
            )
        )

    frappe.db.bulk_insert(DOCTYPE, fields, rows)
    frappe.db.commit()


def import_kabupaten_kota():
    DOCTYPE = "Kabupaten Atau Kota"

    file_path = os.path.join(
        frappe.get_app_path("wilayah_id"),
        "json",
        "kabupaten_atau_kota.json"
    )

    if not os.path.exists(file_path):
        frappe.throw(f"Seed file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    fields = [
		"name",
        "kabupaten_kota",
        "zone_code",
        "provinsi"
	]
    for row in data:
        # CEGAH DUPLIKASI
        if frappe.db.exists(DOCTYPE, row.get("name")):
            continue

        rows.append(
            (
                row.get("name"),
                row.get("kabupaten_kota"),
                row.get("zone_code"),
                row.get("provinsi")
            )
        )

    frappe.db.bulk_insert(DOCTYPE, fields, rows)
    frappe.db.commit()


def import_kecamatan():
    DOCTYPE = "Kecamatan"

    file_path = os.path.join(
        frappe.get_app_path("wilayah_id"),
        "json",
        "kecamatan.json"
    )

    if not os.path.exists(file_path):
        frappe.throw(f"Seed file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    fields = [
		"name",
        "kecamatan",
        "zone_code",
        "provinsi",
        "kabupaten_kota",
	]
    for row in data:
        # CEGAH DUPLIKASI
        if frappe.db.exists(DOCTYPE, row.get("name")):
            continue

        rows.append(
            (
                row.get("name"),
                row.get("kecamatan"),
                row.get("zone_code"),
                row.get("provinsi"),
                row.get("kabupaten_kota")
            )
        )

    frappe.db.bulk_insert(DOCTYPE, fields, rows)
    frappe.db.commit()

def import_kelurahan():
    DOCTYPE = "Desa Atau Kelurahan"

    file_path = os.path.join(
        frappe.get_app_path("wilayah_id"),
        "json",
        "desa_atau_kelurahan.json"
    )

    if not os.path.exists(file_path):
        frappe.throw(f"Seed file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    fields = [
		"name",
        "kelurahan",
        "zone_code",
        "provinsi",
        "kabupaten_kota",
        "kecamatan",
	]
    for row in data:
        # CEGAH DUPLIKASI
        if frappe.db.exists(DOCTYPE, row.get("name")):
            continue

        rows.append(
            (
                row.get("name"),
                row.get("kelurahan"),
                row.get("zone_code"),
                row.get("provinsi"),
                row.get("kabupaten_kota"),
                row.get("kecamatan")
            )
        )

    frappe.db.bulk_insert(DOCTYPE, fields, rows)
    frappe.db.commit()