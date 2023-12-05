let partnerId = window.location.pathname.split("/").at(-1);

frappe.pages["partner-details"].on_page_load = function (wrapper) {
  new PartnerDetailsPage(wrapper);
};

const PartnerDetailsPage = Class.extend({
  init: function (wrapper) {
    this.page = frappe.ui.make_app_page({
      parent: wrapper,
      name: "partner-details",
      title: __("Partner Details View"),
      single_column: true,
    });

    this.showPartnerDetails();
  },

  showPartnerDetails: function () {
    //get partner details for coming partner id.
    this.getPartnerDetails();

    //push dom element to page container through frappe method
    $(frappe.render_template(frappe.partnerDetails.body, this)).appendTo(
      this.page.main
    );
  },

  getPartnerDetails: function () {
    frappe.call({
      method:
        "switch_my_loan.switch_my_loan.page.partner_details.partner_details.get_partner_details",
      args: {
        partner_id: partnerId,
      },
      callback: function (r) {
        console.log(r.message);
        // frappe.partnerDetails.showPartnerDetails(r?.message[0] || {});
      },
    });
  },
});

const dashboardIcon = '<i class="fa fa-dashboard fa-2x"></i>';
const userIcon = '<i class="fa fa-user fa-2x"></i>';
const downloadReportIcon = '<i class="fa fa-download fa-2x"></i>';

let partnerDetailsBodyContent = `<div class="row">
<!-- side bar -->
<div class="col-2 border d-flex flex-column align-items-center text-center pt-3 rounded" style="background-color: #312783; height: 100vh">
    <a href="http://localhost:8000/app/sml-partners" onclick="location.reload()" class="text-white"><span class="d-block text-center">${dashboardIcon}</span>Dashboard</a><br>
    <a href="#link2" class="text-white"><span class="d-block text-center">${userIcon}</span>User Management</a><br>
    <a href="#link3" class="text-white"><span class="d-block text-center">${downloadReportIcon}</span>Download Reports</a>
</div>

<!-- main content -->
<div class="col-10" style="height: 100vh; padding-left: 4rem">
    <!-- First Row in col-10 -->
    <div class="row">
        <!-- Tab Navigation -->
        <ul class="nav nav-tabs">
            <li class="nav-item">
                <a class="nav-link active" onclick="toggleTab(1)" data-toggle="tab">Basic Details</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" onclick="toggleTab(2)" data-toggle="tab">Partner KYC</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" onclick="toggleTab(3)" data-toggle="tab">Bank Details</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" onclick="toggleTab(4)" data-toggle="tab">Verification</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" onclick="toggleTab(5)" data-toggle="tab">Agreements</a>
            </li>
        </ul>
    </div>
	<!-- Tab Content -->
	  <div class="row tab-content">
		 <div id="tab1Content" class="tab-pane fade show active">
			<p>Content for Tab 1</p>
		 </div>
		 <div id="tab2Content" class="tab-pane fade">
			<p>Content for Tab 2</p>
		 </div>
		 <div id="tab3Content" class="tab-pane fade">
			<p>Content for Tab 3</p>
		 </div>
		 <div id="tab4Content" class="tab-pane fade">
			<p>Content for Tab 4</p>
		 </div>
		 <div id="tab5Content" class="tab-pane fade">
			<p>Content for Tab 5</p>
		 </div>
	 </div>
</div>`;

const toggleTab = (tab) => {
  // get nav tabs
  const navTabs = document.querySelectorAll(".nav-tabs a");

  // remove active class from all nav tabs
  navTabs.forEach((tab) => {
    tab.classList.remove("active");
  });

  // add active class to the clicked nav tab
  navTabs[tab - 1].classList.add("active");

  // get tab content
  const tab1Content = document.querySelector("#tab1Content");
  const tab2Content = document.querySelector("#tab2Content");
  const tab3Content = document.querySelector("#tab3Content");
  const tab4Content = document.querySelector("#tab4Content");
  const tab5Content = document.querySelector("#tab5Content");

  // mapping of tabs with tab contents
  const mapping = {
    1: tab1Content,
    2: tab2Content,
    3: tab3Content,
	4: tab4Content,
	5: tab5Content,
  };

  // remove show active from all tabs content
  Object.values(mapping).forEach((tabContent) => {
    tabContent.classList.remove("show", "active");
  });

  // add show active to the clicked tab content
  mapping[tab].classList.add("show", "active");
};

const showPartnerDetails = (partnerData) => {
  const partnerDetailsPage = document.querySelector("#partnerDetails");
};

frappe.partnerDetails = {
  body: partnerDetailsBodyContent,
  showPartnerDetails,
};
