// Copyright (c) 2025, ahmed atef and contributors
// For license information, please see license.txt

frappe.ui.form.on("Send Email Record", {
  refresh(frm) {
    if (!frm.doc.status && !frm.is_new()) {
      frm.add_custom_button("Send Email", () => {
        frm.call("send").then(() => {
          frappe.msgprint("Email Sent Successfully");
        });
      });
    }
  },
});
