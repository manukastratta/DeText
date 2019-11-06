// Recieves
chrome.runtime.onMessage.addListener(function(request, sender) {
    if (request.action == "getSource") {
      message.innerText = request.source;
      $.post("http://127.0.0.1:5000/", {html:request.source},
          function (response) {
             // send response to the content script to be displayed
             chrome.runtime.sendMessage({
               method: "contentWarning",
               meaning: response
             });
          });
      message.innerText = ;
    }
});

// sends HTML string to server
function sendToServer(info) {
    // pass selected text to gunicorn server
    $.post("http://127.0.0.1:5000/", {selection:info.selectionText},
        function (response) {
				   // send response to the content script to be displayed
				   chrome.tabs.sendMessage(tabs[0].id, {method: "contentWarning", meaning: response});
	      });
}
