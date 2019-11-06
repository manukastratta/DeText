// Recieves
chrome.runtime.onMessage.addListener(function(request, sender) {
    if (request.action == "getSource") {
      // message.innerText = request.source;
      console.log("http://127.0.0.1:5000/")
      // chrome.runtime.sendMessage({
      //     action: "contentWarning",
      //     source: "<h1>es</h1>"
      // });
      $.post("http://127.0.0.1:5000/", {html:request.source},
        function (response) {
          console.log("resp: " + JSON.stringify(response))
          // chrome.tabs.executeScript(null, {
          //   file: "getPagesSource.js"
          // });
         // chrome.tabs.query({active:true, currentWindow: true},
          // function(tabs) {
          //     // send response to the content script to be displayed
          //     chrome.tabs.sendMessage(tabs[0].id, {method: "contentWarning", meaning: "help"});
          // });
      });
          // send response to the content script to be displayed
  }
});

// function appListener(request, sender) {
//      if (request.action == "contentWarning") {
//        $.post("http://127.0.0.1:5000/", {html:request.source});
//      }
// }
