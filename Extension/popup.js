chrome.runtime.onMessage.addListener(function(request, sender) {
    if (request.action == "getSource") {
//       //message.innerText = request.source;
//       console.log("http://127.0.0.1:5000/")
//       $.post("http://127.0.0.1:5000/", {html:request.source},
//           function (response) {
//              // send response to the content script to be displayed
//              chrome.runtime.sendMessage({
//                 method: "contentWarning",
//                 meaning: response
//              });
//           });
      message.innerText = request.source
    }
});

//Injects script into tab to extract HTML
function onWindowLoad() {
  var message = document.querySelector('#message');

  chrome.tabs.executeScript(null, {
    file: "getPagesSource.js"
  }, function() {
    // If you try and inject into an extensions page or the webstore/NTP you'll get an error
    if (chrome.runtime.lastError) {
      message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
    }
  });
}

window.onload = onWindowLoad;

// listen for a response from the app.js script
chrome.runtime.onMessage.addListener(function(request, sender) {
     if (request.action == "contentWarning") {
       //Recieves response from server that can be used to modify popup.html

     }
});

// $(function() {
//     $('#name').keyup(function() {
//         $('#greet').text('Hello ' + $('#name').val());
//     })
// })
