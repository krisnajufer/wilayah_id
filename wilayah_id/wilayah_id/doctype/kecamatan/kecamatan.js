// Copyright (c) 2025, Jufer and contributors
// For license information, please see license.txt

frappe.ui.form.on("Kecamatan", {
	refresh(frm) {
        Filterwilayah(frm)
	},
    provinsi(frm){
        Filterwilayah(frm)
    }
});


function Filterwilayah(frm){
    frm.set_query("kabupaten_kota", (doc) => {
        return {
            filters: {
                provinsi: ["=", doc.provinsi]
            }
        }
    })
}