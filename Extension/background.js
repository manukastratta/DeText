chrome.runtime.onMessage.addListener(function(request, sender) {
    if (request.action == "getSource") {
      // message.innerText = request.source;
      console.log("http://127.0.0.1:5000/")
      console.log("HELLO THERE")

      $.post("http://127.0.0.1:5000/", {html:request.source},
        function (response) {
        console.log("THIS IS WHAT THE RESPONSE SHOULD LOOK LIKE");
        console.log(response)
        console.log(response.trigger)
          if (response.trigger) {
              window.confirm("Warning: this website may contain content related to sexual violence that could be disturbing for some users.");
          }
      });
  }
});