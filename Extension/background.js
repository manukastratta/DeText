// Recieves
chrome.runtime.onMessage.addListener(function(request, sender) {
    if (request.action == "getSource") {
      // message.innerText = request.source;
      console.log("http://127.0.0.1:5000/")

      $.post("http://127.0.0.1:5000/", {html:request.source},
        function (response) {
          alert(response.text)
          // window.confirm("Warning: this website may contain content that could be disturbing for some users");
          chrome.runtime.sendMessage({
              action: "contentWarning",
              source: "hello"
          });
      });
  }
});

window.onload = onWindowLoad;

//  chrome.tabs.executeScript(null, {file: "background.js"})