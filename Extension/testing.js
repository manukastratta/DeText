

//scanForContent()
scanForContent2()

function scanForContent() {
    document.write('Hello world')
}

// IS BEING CALLED!
function scanForContent2() {
  const message = document.querySelector('#message');

  chrome.tabs.executeScript(null, {
    file: "getPagesSource.js"
  }, function() {
    // If you try and inject into an extensions page or the webstore/NTP you'll get an error
    if (chrome.runtime.lastError) {
      message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
    }
  });
}