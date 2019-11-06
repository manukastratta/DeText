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
  // chrome.tabs.executeScript(null, {file: "app.js"})
}

window.onload = onWindowLoad;


// listen for a message from the app.js script
if (!chrome.runtime.onMessage.hasListener(appListener)) {
    chrome.runtime.onMessage.addListener(appListener);
    // console.log("event heard around the world")
}

// listen for a response from the app.js script
function appListener(request, sender) {
     if (request.action == "contentWarning") {
        message.innerText = request.source;
     }
}

// $(function() {
//     $('#name').keyup(function() {
//         $('#greet').text('Hello ' + $('#name').val());
//     })
// })
