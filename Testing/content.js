console.log("Chrome extension ready to go!")
// var myDiv=document.createElement("myDiv");
// document.body.appendChild(myDiv);
// myDiv.innerText="TEST123";


function injectStyles() {
  // Injecting css style is-blurred to html of page
  // var styleBlurred = document.createElement('style');
  //   styleBlurred.innerHTML = `
  //   .is-blurred {
  //     filter: blur(1px);
  //   }
  //   `;
  // document.head.appendChild(styleBlurred);

  var styleNoBlur = document.createElement('style');
    styleNoBlur.innerHTML = `
    .no-blurr {
      filter: none;
    }
    `;
  document.head.appendChild(styleNoBlur);

  var styleModal = document.createElement('style');
    styleModal.innerHTML = `
    .Modal {
      display: block;
      position: fixed;
      left: 0;
      top: 0;
      z-index: 9999;
      width: 100%;
      height: 100%;
      padding-top: 100px;
      background-color: rgba(0, 100, 0, 0.4);
      overflow: auto;
      transition: all 0.5s linear;
    }
    `;
  document.head.appendChild(styleModal);

  var styleModalContent = document.createElement('style');
    styleModalContent.innerHTML = `
    .Modal-content {
      background-color: white;
      margin: auto;
      padding: 20px;
      border-radius: 4px;
      max-width: 350px;
      height: 200px;
    }
    `;
  document.head.appendChild(styleModalContent);

  var styleHidden = document.createElement('style');
    styleHidden.innerHTML = `
      .is-hidden { display: none; }
    `;
  document.head.appendChild(styleHidden);

  var styleVisuallyHidden = document.createElement('style');
    styleVisuallyHidden.innerHTML = `
      .is-visuallyHidden { opacity: 0; }
    `;
  document.head.appendChild(styleVisuallyHidden);

  var styleClose = document.createElement('style');
    styleClose.innerHTML = `
      .Close {
        color: black;
        float: right;
        font-size: 16px;
      }
    `;
  document.head.appendChild(styleClose);

//   body > *:not(#loading) {
//   filter: blur(3px);
// }


}

//injectStyles()

// Button for testing. Open the modal.
// var page = document.getElementById("body");
// if(!page) {
//   page = document.getElementById("main");
// }
// if(!page) {
//   page = document.getElementById("html");
// }
var page = document.body;
var button = document.createElement("button");
var text = document.createTextNode("TEST BUTTON");
button.appendChild(text);
page.appendChild(button);

// Initially, page is not blurred
var isBlurred = false;

button.onclick=function(){
  if(!isBlurred) {
    //document.body.classList.add("is-blurred");
    isBlurred = true;
    //$('body').not("#loading").css("filter","blur(3px)");
    showModalContent();
  }
}

// Creating modal div
var modalDiv = document.createElement('div');
modalDiv.className = 'Modal no-blurr is-hidden is-visuallyHidden';
modalDiv.innerHTML = `
  <div class="Modal-content no-blurr">
      <span id="closeModal" class="Close">&times;</span>
      <h2><img src="icon-48x48.png" alt="" /> DeText Warning</h2>
      <h3>This website may contain content related to sexual
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
  hideModalContent();
}
