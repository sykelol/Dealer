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

// JavaScript code to update the current step
var currentStep = "{{ wizard.steps.current }}"; // get the current step from Django
var stepList = document.querySelector('.wizard-step-active');
var stepItems = stepList.querySelectorAll('li');
for (var i = 0; i < stepItems.length; i++) {
  stepItems[i].classList.remove('active');
}
var currentStepItem = stepList.querySelector('h5:contains(' + currentStep + ')').parentNode;
currentStepItem.classList.add('active');