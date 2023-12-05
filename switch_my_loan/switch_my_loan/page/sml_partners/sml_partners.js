frappe.pages["sml-partners"].on_page_load = function (wrapper) {
  new SmlPartnersDashboard(wrapper);
};

SmlPartnersDashboard = Class.extend({
  init: function (wrapper) {
    this.page = frappe.ui.make_app_page({
      parent: wrapper,
      name: "sml-partners",
      title: __("SML Partners"),
      single_column: true,
    });

    this.makeDashboard();
  },

  makeDashboard: function () {
    //get total partners
    this.getAllPartners();

    //push dom element to page container through frappe method
    $(frappe.render_template(frappe.smlDashboardPage.body, this)).appendTo(
      this.page.main
    );

    // refresh the page
    document.querySelector("#refresh-btn").addEventListener("click", () => {
      this.refreshPage();
    });

    // filter by user type
    document.querySelector("#userTypeSelect").addEventListener("change", () => {
      this.filterByUserType();
    });

    // filter by user status
    document
      .querySelector("#userStatusSelect")
      .addEventListener("change", () => {
        this.filterByUserType();
      });

    // advanced filter
    document
      .querySelector("#advancedFilterBtn")
      .addEventListener("click", () => {
        this.advancedFilter();
      });

    // date filter
  },

  refreshPage: function () {
    document.querySelector("#userTypeSelect").value = "";
    document.querySelector("#userStatusSelect").value = "";
    this.getAllPartners();
  },

  getAllPartners: function () {
    frappe.call({
      method:
        "switch_my_loan.switch_my_loan.page.sml_partners.sml_partners.get_partners",
      callback: function (r) {
        console.log(r.message);
        frappe.smlDashboardPage.partnerTableBody(r?.message);
      },
    });
  },

  filterByUserType: function () {
    frappe.call({
      method:
        "switch_my_loan.switch_my_loan.page.sml_partners.sml_partners.filter_by_user_type",
      args: {
        partner_type_value:
          document.querySelector("#userTypeSelect").value || "",
        user_status_value:
          document.querySelector("#userStatusSelect").value || "",
      },
      callback: function (r) {
        console.log(r.message);
        frappe.smlDashboardPage.partnerTableBody(r?.message);
      },
    });
  },

  advancedFilter: function () {
    const fieldName = document.querySelector("#filterField").value || "";
    const fieldValue = document.querySelector("#filterValue").value || "";
    const createdAtStartDate = document.querySelector("#start").value || "";
    const createdAtEndDate = document.querySelector("#end").value || "";
    const enableColumn1 = document.querySelector("#enableColumn1").checked;
    const enableColumn2 = document.querySelector("#enableColumn2").checked;
    if ((fieldName && fieldValue) || (createdAtStartDate && createdAtEndDate)) {
      frappe.call({
        method:
          "switch_my_loan.switch_my_loan.page.sml_partners.sml_partners.advanced_search",
        args: {
          field_name: fieldName,
          field_value: fieldValue,
          created_at_start_date: createdAtStartDate,
          created_at_end_date: createdAtEndDate,
          enable_column1: enableColumn1,
          enable_column2: enableColumn2,
        },
        callback: function (r) {
          console.log(r.message);
          document.querySelector("#filterField").value = "";
          document.querySelector("#filterValue").value = "";
          document.querySelector("#start").value = "";
          document.querySelector("#end").value = "";
          document.querySelector("#enableColumn1").checked = false;
          document.querySelector("#enableColumn2").checked = false;
          frappe.smlDashboardPage.partnerTableBody(r?.message);
        },
      });
    } else return;
  },
});

//render template (body of the page)
const dashboardIcon = '<i class="fa fa-dashboard fa-2x"></i>';
const userIcon = '<i class="fa fa-user fa-2x"></i>';
const downloadReportIcon = '<i class="fa fa-download fa-2x"></i>';
const filterIcon = '<i class="fa fa-filter"></i>';
const refreshIcon = '<i class="fa fa-refresh"></i>';

let bodyContent = `<div class="row">
<!-- side bar -->
<div class="col-2 border d-flex flex-column align-items-center text-center pt-3 rounded" style="background-color: #312783; height: 100vh">
    <a href="partner-details" class="text-white"><span class="d-block text-center">${dashboardIcon}</span>Dashboard</a><br>
    <a href="#link2" class="text-white"><span class="d-block text-center">${userIcon}</span>User Management</a><br>
    <a href="#link3" class="text-white"><span class="d-block text-center">${downloadReportIcon}</span>Download Reports</a>
</div>

<!-- main content -->
<div class="col-10 pt-3" style="height: 100vh">
    <!-- First Row in col-10 -->
    <div class="row">
        <div class="col-md-4">
            <select id="userTypeSelect" class="form-select p-2 rounded" aria-label="Dropdown 1">
                <option value="">User Type</option>
                <option value="partner_individual">Partner-Individual</option>
                <option value="partner_corporate">Partner-Corporate</option>
                <option value="customer">Customer</option>
                <option value="all">All</option>
            </select>
            <select id="userStatusSelect" class="form-select p-2 rounded" aria-label="Dropdown 2">
                <option value="">Status</option>
                <option value="New">New User</option>
                <option value="pending_at_user">Pending At User</option>
                <option value="pending_at_sml">Pending At SML</option>
                <option value="registered_user">Registered User</option>
                <option value="all">All</option>
            </select>
        </div>

        <!-- Search Bar -->
        <div class="col-md-8">
        <div class="d-inline">
            <!-- <input class="form-control mb-1" type="search" placeholder="Search" aria-label="Search"/>
            <button class="btn text-white ml-1" type="submit" style="float: right; background-color: #E30613"">Search</button> -->
  
            <button id="refresh-btn"class="btn text-white ml-1" style="float: right; background-color: #E30613"><span>${refreshIcon}</span> Refresh</button>
            <!-- Button trigger modal -->
            <button type="button" style="float: right; background-color: #E30613" class="btn text-white" data-toggle="modal" data-target="#exampleModalCenter">
            <span>${filterIcon}</span> Advanced Filter
            </button>
        </div>
        </div>
    </div>

    <!-- Second Row in col-10 (Table) -->
    <div class="row">
        <div class="col">
            <table class="table table-hover table-striped">
                <thead>
                    <tr>
                        <th scope="col">Created At</th>
                        <th scope="col">User Id</th>
                        <th scope="col">Name</th>
                        <th scope="col">Location</th>
                        <th scope="col">User Type</th>
                        <th scope="col">Mobile</th>
                        <th scope="col">E-mail</th>
                        <th scope="col">Approval Date</th>
                        <th scope="col">Status</th>
                    </tr>
                </thead>
                <tbody id="showPartners">
                </tbody>
            </table>
        </div>
    </div>
</div>
</div>

<!-- Modal -->
<div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLongTitle">Advanced Filter</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>

      <div class="modal-body">
      <div class="text-center bold mb-3">Choose Filter Options</div>
        <!-- Two-column layout -->
        <div class="row d-flex justify-content-center">
          <!-- First Column -->
          <div class="col-5"> 
              <div class="mb-2">
                <input type="checkbox" id="enableColumn1" onclick="toggleColumn(1)"> Enable field Filter
              </div>
              <div class="mb-2">
                <label for="filterField" class="form-label">FieldName:</label>
                <select id="filterField" class="form-select d-block form-control" disabled>
                  <option value="">Select Option</option>
                  <option value="first_name">Name</option>
                  <option value="phone">Mobile</option>
                  <option value="email">E-mail</option>
                  <option value="city">Location</option>
                </select>
              </div>
              <div>
                <label for="filterValue" class="form-label">Value:</label>
                <input type="text" id="filterValue" class="form-control" placeholder="Enter Value" disabled>
              </div>
          </div>
          <div class="border-left" style="border: 1px solid black"></div>
          <div class="col-6">
           <div class="mb-2">      
             <input type="checkbox" id="enableColumn2" onclick="toggleColumn(2)"> Enable Date Filter
           </div>
              <div class="col p-0">
                <div class="mb-2">
                <label for="start" >CreatedAt StartDate : </label>
                <input class="p-1 rounded w-100 form-control" type="date" id="start" disabled>
                </div>
                <div>
                <label for="end" >CreatedAt EndDate : </label>
                <input class="p-1 rounded w-100 form-control" type="date" id="end" disabled>
                </div>
              </div>
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" id="advancedFilterBtn" style="float: right; background-color: #E30613" class="btn text-white" data-dismiss="modal">Submit</button>
      </div>
    </div>
  </div>
</div>`;

function createTableBodyAsPerGivenData(partners) {
  let length = partners.length;
  let partnerTable = document.querySelector("#showPartners");
  partnerTable.innerHTML = "";
  if (length == 0) {
    partnerTable.innerHTML = `<tr><td colspan="9" class="text-center">No Data Available</td></tr>`;
    return;
  } else {
    partners.map((partner) => {
      const { partner_id, first_name, last_name, created_at } = partner;
      const { phone, email, approved_at, partner_type, city, status } = partner;
      partnerTable.innerHTML += `<tr><td>${created_at}</td>
       <td><a href="partner-details/${partner_id}" onclick="location.reload()" class="text-primary">${partner_id}</a></td>
       <td>${first_name + " " + last_name}</td>
       <td>${city}</td>
       <td>${partner_type}</td>
       <td>${phone}</td>
       <td>${email}</td>
       <td>${approved_at || ""}</td>
       <td>${status || ""}</td></tr>`;
    });
  }
}

function toggleColumn(columnNumber) {
  // Determine which elements to enable/disable based on the column number
  console.log(columnNumber);
  var elementsToToggle =
    columnNumber === 1
      ? document.querySelectorAll("#filterField, #filterValue")
      : document.querySelectorAll("#start, #end");

  // Toggle enable/disable state
  elementsToToggle.forEach((element) => {
    element.disabled = !element.disabled;
  });
}

frappe.smlDashboardPage = {
  body: bodyContent,
  partnerTableBody: createTableBodyAsPerGivenData,
};
