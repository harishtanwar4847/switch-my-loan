// Copyright (c) 2024, Atrina Technologies Pvt Ltd and contributors
// For license information, please see license.txt
const nucleusBaseUrlByHostNameMap = {
  localhost: "http://localhost:3000",
  "uat-crm.switchmyloan.in": "http://3.6.162.163:4000",
  "mycrm.switchmyloan.in": "https://nucleus.switchmyloan.in",
};

const nucleusBaseUrl = nucleusBaseUrlByHostNameMap[document.location.hostname];

async function updateStatusInApiServer(frm) {
  try {
    await fetch(`${nucleusBaseUrl}/partner/updatePartnerInfo`, {
      method: "POST",
      body: JSON.stringify({
        authId: frm.doc.partner_id,
        updateFields: {
          status: frm.doc.status.toLowerCase().replaceAll(" ", "_"),
        },
      }),
      headers: { "Content-Type": "application/json" },
    });
    return true;
  } catch (error) {
    console.log("updateStatusInApiServer ~ error:", error);
    return false;
  }
}

frappe.ui.form.on("SML Partner", {
  //   refresh: function (frm) {

  //   },

  referrer_type: function (frm) {
    if (
      ["SML Employee", "Another Partner"].some((e) =>
        e.includes(frm.doc.referrer_type)
      )
    ) {
      frm.toggle_display("referrer_name", true);
      if (frm.doc.referrer_type.includes("SML")) {
        frm.toggle_display("referrer_email", true);
      }
    } else {
      frm.toggle_display("referrer_name", false);
      frm.toggle_display("referrer_email", false);
    }
  },

  status: async function (frm) {
    await frappe.db.set_value(
      "SML Partner",
      frm.doc.name,
      "status",
      frm.doc.status
    );
    await updateStatusInApiServer(frm);
    frm.reload_doc();
  },
});
