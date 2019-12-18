// Received message from content.js. Sends POST request to Python server
chrome.runtime.onMessage.addListener(function(request, sender) {
    if (request.action == "getSource") {
      // message.innerText = request.source;
      //console.log("RECEIVED MESSAGE")

      $.post("http://stark-meadow-27357.herokuapp.com/", {html:request.source},
        function (response) {
        // If decision to display content warning is positive
          if (response.trigger) {
              window.confirm("Warning: this website may contain content related to sexual violence that could be disturbing for some users.");
          }
      });
  }
});


//////Injects script into tab to extract HTML
////function scanForContent() {
////  const message = document.querySelector('#message');
////
////  chrome.tabs.executeScript(null, {
////    file: "getPagesSource.js"
////  }, function() {
////    // If you try and inject into an extensions page or the webstore/NTP you'll get an error
////    if (chrome.runtime.lastError) {
////      message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
////    }
////  });
////}
////
////window.onload = scanForContent;
