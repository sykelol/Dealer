const sideButton = document.querySelector("#sidebar-menu-icon");
const sidebar = document.querySelector(".dashboard-sidebar");
const activeLink = document.querySelector(".dashboard-link");
const sideButtonFirst = document.querySelector("#sidebar-menu-icon-first");


/* document.getElementById("drivers_license").value = "{{ form.drivers_license.value.url }}" */

sideButton.onclick = function() {
    sidebar.classList.toggle("active");
};

sideButtonFirst.onclick = function() {
    sidebar.classList.toggle("active");
};

/*
function navigateToStep(step) {
    const form = document.getElementById('wizard-form');
    form.elements['wizard_goto_step'].value = step;
    form.submit();
  }
  
  function submitForm() {
    const form = document.getElementById('wizard-form');
    form.elements['wizard_goto_step'].value = 'done';
    form.submit();
  }
*/
