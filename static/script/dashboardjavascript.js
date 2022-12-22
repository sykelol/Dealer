const sideButton = document.querySelector("#sidebar-menu-icon");
const sidebar = document.querySelector(".dashboard-sidebar");
const activeLink = document.querySelector(".dashboard-link");
const sideButtonFirst = document.querySelector("#sidebar-menu-icon-first");
const statusChange = document.querySelector("#table-status");
const dealChange = document.querySelector("#deal-status");
const table = document.querySelector("#mydeals_table");
const cells = table.getElementsByTagName("td");

sideButton.onclick= function() {
    sidebar.classList.toggle("active");
};

sideButtonFirst.onclick= function() {
    sidebar.classList.toggle("active");
};

for (var i = 0; i < dealChange.length; i++) {
    var paragraphs = dealChange[i].getElementsByTagName("p");
    if (paragraphs[0].innerHTML == "pending") {
        dealChange[i].style.backgroundColor = "yellow";
    }
};