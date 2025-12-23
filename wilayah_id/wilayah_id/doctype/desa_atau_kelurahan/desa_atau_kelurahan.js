// Copyright (c) 2025, Jufer and contributors
// For license information, please see license.txt

frappe.ui.form.on("Desa Atau Kelurahan", {
	refresh(frm) {
        Filterwilayah(frm)
	},
	provinsi(frm) {
        Filterwilayah(frm)
	},
	kabupaten_kota(frm) {
        Filterwilayah(frm)
	},
});

function Filterwilayah(frm){
    frm.set_query("kabupaten_kota", (doc) => {
        return {
            filters: {
                provinsi: ["=", doc.provinsi]
            }
        }
    })
    frm.set_query("kecamatan", (doc) => {
        return {
            filters: {
                provinsi: ["=", doc.provinsi],
                kabupaten_kota: ["=", doc.kabupaten_kota]
            }
        }
    })
}