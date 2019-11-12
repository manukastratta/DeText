// // To print the html to the screen
// chrome.runtime.onMessage.addListener(function(request, sender) {
//   if (request.action == "getSource") {
//     message.innerText = request.source;
//   }
// });

//Injects script into tab to extract HTML
function onWindowLoad() {
  const message = document.querySelector('#message');

  chrome.tabs.executeScript(null, {
    file: "getPagesSource.js"
  }, function() {
    // If you try and inject into an extensions page or the webstore/NTP you'll get an error
    if (chrome.runtime.lastError) {
      message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
    }
  });
  // chrome.tabs.executeScript(null, {file: "background.js"})
}

window.onload = onWindowLoad;


// listen for a message from the background.js script
if (!chrome.runtime.onMessage.hasListener(appListener)) {
    chrome.runtime.onMessage.addListener(appListener);
    // console.log("event heard around the world")
}

// listen for a response from the background.js script
function appListener(request, sender) {
  console.log("heard request", request.action)
     if (request.action == "contentWarning") {
        message.innerText = request.source;
     }
}
// async function serverResponse() {
//   console.log("yes")
//   const response = await fetch('http://127.0.0.1:5000/');
//   console.log("response recieved")
//   const myJson = await response.json();
//   console.log(JSON.stringify(myJson));
// }
// $(function() {
//     $('#name').keyup(function() {
//         $('#greet').text('Hello ' + $('#name').val());
//     })
// })
