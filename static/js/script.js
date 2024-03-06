const $ = e => document.querySelector(e);
const $$ = e => document.querySelectorAll(e);

// Variables
const app = $(".app");

const pTSecondButton = $(".btn-pTSecond");

const pTFirstButton = $(".btn-pTFirst");


const form = $(".form");
const formInputs = $$(".form__input");
const formButton = $(".btn-form");


// pTSecondButton Events
/* =============================================================================================== */
pTSecondButton.addEventListener("mouseenter", () => {
  app.classList.add("on-btn-pTSecond");
})

pTSecondButton.addEventListener("focus", () => {
  app.classList.add("on-btn-pTSecond");
})

pTSecondButton.addEventListener("mouseleave", () => {
  app.classList.remove("on-btn-pTSecond");
})

pTSecondButton.addEventListener("blur", () => {
  app.classList.remove("on-btn-pTSecond");
})

pTSecondButton.addEventListener("click", () => {
  app.classList.add("second-screen-opened");
  app.classList.remove("on-btn-pTSecond");
})

pTFirstButton.addEventListener("click", () => {
  app.classList.add("on-btn-pTSecond");
  app.classList.remove("second-screen-opened");
})


// Form submit
/* =============================================================================================== */
function register() {
  location.href="/addUser?fromDashBoard=" + false
}


// If the password is wrong, skip the first screen and show the hint
/* =============================================================================================== */
wrongpassword = $("#dataTransForSignIn").dataset.wrongpassword == "True"

if (wrongpassword) {
  pTSecondButton.click();
}