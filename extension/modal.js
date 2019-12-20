//console.log("Chrome extension ready to go!")
// var myDiv=document.createElement("myDiv");
// document.body.appendChild(myDiv);
// myDiv.innerText="TEST123";

// Button for testing. Open the modal.
// var page = document.getElementById("body");
// if(!page) {
//   page = document.getElementById("main");
// }
// if(!page) {
//   page = document.getElementById("html");
// }
var page = document.body;
// var button = document.createElement("button");
// var text = document.createTextNode("TEST BUTTON");
// button.appendChild(text);
// page.appendChild(button);

// Initially, page is not blurred
//var isBlurred = false;

// button.onclick=function(){
//   if(!isBlurred) {
//     //document.body.classList.add("is-blurred");
//     isBlurred = true;
//     $("body > *").not("body > .Modal").css("filter","blur(3px)");
//     //$('body').not('.Modal').css("filter","blur(3px)");
//     showModalContent();
//   }
// }

// Creating modal div
var modalDiv = document.createElement('div');
modalDiv.className = 'Modal no-blurr is-hidden is-visuallyHidden';
modalDiv.innerHTML = `
  <div class="Modal-content no-blurr">
      <span id="closeModal" class="Close">&times;</span>
      <h2 id = "DeTextTitle">DeText Warning</h2>
      <h3 id = "DeTextMessage">This website may contain content related to sexual
          violence that could be disturbing for some users.</h3>
  </div>
`;
page.appendChild(modalDiv);

// Show modal
function showModalContent() {
  modalDiv.classList.remove("is-hidden", "is-visuallyHidden");
}

// Hide modal
function hideModalContent() {
  modalDiv.classList.add("is-hidden", "is-visuallyHidden");
}

// Close modal
btnClose=document.getElementById("closeModal");

btnClose.onclick= function(){
  document.body.classList.remove("is-blurred");
  isBlurred = false;
  $("body > *").not("body > .Modal").css("filter","none");
  hideModalContent();
}


$("body > *").not("body > .Modal").css("filter","blur(3px)");
showModalContent();
