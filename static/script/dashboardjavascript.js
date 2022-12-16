const sideButton = document.querySelector("#sidebar-menu-icon");
const sidebar = document.querySelector(".dashboard-sidebar");
const activeLink = document.querySelector(".dashboard-link");
const sideButtonFirst = document.querySelector("#sidebar-menu-icon-first");

sideButton.onclick= function() {
    sidebar.classList.toggle("active");
};

sideButtonFirst.onclick= function() {
    sidebar.classList.toggle("active");
};