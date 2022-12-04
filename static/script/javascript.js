const primaryNav = document.querySelector('.primary-navigation');
const navToggle = document.querySelector('.mobile-nav-toggle');
const body = document.getElementsByTagName('body');

function openClose() {
    const visibility = primaryNav.getAttribute("data-visible");
    if (visibility === "false") {
        primaryNav.setAttribute("data-visible", true);
        navToggle.setAttribute('aria-expanded', true);
    } else if (visibility === "true") {
        primaryNav.setAttribute("data-visible", false);
        navToggle.setAttribute("aria-expanded", false);
    }
};

navToggle.addEventListener('click', openClose());

const vehicleCost = document.getElementById("vehicle-cost-input");
const downPayment = document.getElementById("down-payment-input");
const tradeIn = document.getElementById("trade-in-input");
const interestRate = document.getElementById("interest-rate-input");
const loanDuration = document.getElementById("loan-duration-input");
const financeAmount = document.getElementById("finance-amount");

function monthlyPayments() {
    const vehicleCost = parseInt(document.getElementById("vehicle-cost-input").value);
    const downPayment = parseInt(document.getElementById("down-payment-input").value);
    const tradeIn = parseInt(document.getElementById("trade-in-input").value);
    const interestRate = parseFloat(document.getElementById("interest-rate-input").value);
    const loanDuration = parseInt(document.getElementById("loan-duration-input").value);
    let loanBalance = vehicleCost - downPayment - tradeIn;
    let monthlyInterest = ((interestRate / 100) / 12);
    let payment = (loanBalance * (monthlyInterest * Math.pow(1 + monthlyInterest, loanDuration))) / (Math.pow(1 + monthlyInterest, loanDuration) - 1);
    if (!vehicleCost) {
        return;
    }
    if (!interestRate) {
        return;
    }
    if (!loanDuration) {
        return;
    }
    if (loanBalance < 0) {
        return;
    }
    let rounded = parseFloat(Math.round(payment * 100) / 100);
    financeAmount.innerHTML = ("$" + rounded.toLocaleString('en'));
}

/*

function floatNumber() {
    const vehicleCost = parseFloat(document.getElementById("vehicle-cost-input").value);
    const downPayment = parseFloat(document.getElementById("down-payment-input").value);
    const tradeIn = parseFloat(document.getElementById("trade-in-input").value);
    if (vehicleCost) {
        financeAmount.innerHTML = ("$" + vehicleCost.toLocaleString('en'));
    }
    if (downPayment) {
        financeAmount.innerHTML = ("$" + downPayment.toLocaleString('en'));
    }
    if (tradeIn) {
        financeAmount.innerHTML = ("$" + tradeIn.toLocaleString('en'));
    }
}

*/

function maxMinValue() {
    const vehicleCost = (document.getElementById("vehicle-cost-input").value);
    const downPayment = (document.getElementById("down-payment-input").value);
    const tradeIn = (document.getElementById("trade-in-input").value);
    const interestRate = (document.getElementById("interest-rate-input").value);
    const loanDuration = (document.getElementById("loan-duration-input").value);
    if (vehicleCost > 150000) {
        document.getElementById("vehicle-cost-input").value = 150000;
    }
    if (vehicleCost < 0) {
        document.getElementById("vehicle-cost-input").value = 0;
    }
    if (downPayment > 150000) {
        document.getElementById("down-payment-input").value = 150000;
    }
    if (downPayment < 0) {
        document.getElementById("down-payment-input").value = 0;
    }
    if (tradeIn > 150000) {
        document.getElementById("trade-in-input").value = 150000;
    }
    if (tradeIn < 0) {
        document.getElementById("trade-in-input").value = 0;
    }
    if (interestRate > 100) {
        document.getElementById("interest-rate-input").value = 100;
    }
    if (interestRate < 0) {
        document.getElementById("interest-rate-input").value = 0;
    }
    if (loanDuration > 96) {
        document.getElementById("loan-duration-input").value = 96;
    }
    if (loanDuration < 0) {
        document.getElementById("loan-duration-input").value = 0;
    }
}


vehicleCost.addEventListener('onblur', maxMinValue());
vehicleCost.addEventListener('onkeyup', monthlyPayments());

downPayment.addEventListener('onblur', maxMinValue());
downPayment.addEventListener('onkeyup', monthlyPayments());

tradeIn.addEventListener('onblur', maxMinValue());
tradeIn.addEventListener('onkeyup', monthlyPayments());

interestRate.addEventListener('onblur', maxMinValue());
interestRate.addEventListener('onkeyup', monthlyPayments());

loanDuration.addEventListener('onblur', maxMinValue());
loanDuration.addEventListener('onkeyup', monthlyPayments());


const sideButton = document.querySelector("#sidebar-menu-icon");
const sidebar = document.querySelector(".dashboard-sidebar");



sideButton.onclick= function() {
    sidebar.toggle(" active");
};