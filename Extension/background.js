// Recieves
chrome.runtime.onMessage.addListener(function(request, sender) {
    if (request.action == "getSource") {
      // message.innerText = request.source;
      console.log("http://127.0.0.1:5000/")

      $.post("http://127.0.0.1:5000/", {html:request.source},
        function (response) {
          if (response.trigger) {
              window.confirm("Warning: this website may contain content that could be disturbing for some users. \n(TW: Sexual Content)");
          }
      });
  }
});

window.onload = onWindowLoad;

//  chrome.tabs.executeScript(null, {file: "background.js"})