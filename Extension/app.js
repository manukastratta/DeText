// Recieves
chrome.runtime.onMessage.addListener(function(request, sender) {
    if (request.action == "getSource") {
      //message.innerText = request.source;
      console.log("http://127.0.0.1:5000/")
      $.post("http://127.0.0.1:5000/", {html:request.source},
          function (response) {
             // send response to the content script to be displayed
             chrome.runtime.sendMessage({
                method: "contentWarning",
                meaning: response
             });
          });
    }
});
