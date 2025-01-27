frappe.listview_settings["Send Email Record"] = {
  get_indicator: (doc) => {
    const status_colors = {
      "Delivered": "green",
      "Sent": "blue",
      "Delivery Delayed": "pink",
      "Complained": "orange",
      "Opened": "cyan",
      "Bounced":"red"
    };
    return [
      doc.status || "No Status",
      status_colors[doc.status] || "gray",
      "status,=," + doc.status,
    ];
  },
};
