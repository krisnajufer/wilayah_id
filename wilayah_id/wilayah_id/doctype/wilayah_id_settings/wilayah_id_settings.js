// Copyright (c) 2025, Jufer and contributors
// For license information, please see license.txt

frappe.ui.form.on("Wilayah ID Settings", {
    refresh(frm){
        frm.disable_save()
    },
	async reset(frm) {
        await frappe.call({
                    method: 'wilayah_id.wilayah_id.doctype.wilayah_id_settings.wilayah_id_settings.reset',
                    freeze: true,
                    freeze_message: __("Reseting Wilayah ID to Default"),
                    callback: (r) => {
                    // on success
                        frappe.msgprint("Success Reset Wilayah ID to Default")
                    },
                    error: (r) => {
                    // on error
                    }
                })
	},
});