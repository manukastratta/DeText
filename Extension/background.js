// Recieves
chrome.runtime.onMessage.addListener(function(request, sender) {
    if (request.action == "getSource") {
      // message.innerText = request.source;
      console.log("http://127.0.0.1:5000/")
      // chrome.runtime.sendMessage({
      //     action: "contentWarning",
      //     source: "hello"
      // });
      $.post("http://127.0.0.1:5000/", {html:request.source},
        function (response) {
          console.log("resp: " + JSON.stringify(response));
          chrome.runtime.sendMessage({
              action: "contentWarning",
              source: "hello"
          });
          // message.innerText = JSON.stringify(response);
         // chrome.tabs.query({active:true, currentWindow: true},
         //  function(tabs) {
         //      // send response to the content script to be displayed
         //      chrome.tabs.sendMessage(tabs[0].id, {method: "contentWarning", source: "help"});
         //  });
      });
          // send response to the content script to be displayed
  }
});

// function appListener(request, sender) {
//      if (request.action == "contentWarning") {
//        $.post("http://127.0.0.1:5000/", {html:request.source});
//      }
// }
