// Copyright (c) 2025, ahmed atef and contributors
// For license information, please see license.txt

frappe.ui.form.on("Send Email Broadcast", {
  refresh(frm) {
    frm.add_custom_button(__("Send Emails"), function () {
      frm.call("send_resend_emails").then(() => {
        frm.reload_doc();
      });
    });
  },
});
