chrome.runtime.onMessage.addListener(function(request, sender) {
    if (request.action == "getSource") {
      message.innerText = request.source;
    }
  });

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

$(function() {
    $('#name').keyup(function() {
        $('#greet').text('Hello ' + $('#name').val());
    })
})

// sends HTML string to server
function lookUpAcronym(info) {
    // pass selected text to gunicorn server
    $.post("http://127.0.0.1:5000/", {selection:info.selectionText},
        function (response) {
	         chrome.tabs.query({active:true, currentWindow: true},
				   function(tabs) {
				         // send response to the content script to be displayed
				         chrome.tabs.sendMessage(tabs[0].id, {method: "displayMeaning", meaning: response});
				   });
	      });
}
