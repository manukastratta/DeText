// //Injects script into tab to extract HTML
// function scanForContent() {
//   const message = document.querySelector('#message');
//
//   chrome.tabs.executeScript(null, {
//     file: "content.js"
//   }, function() {
//     // If you try and inject into an extensions page or the webstore/NTP you'll get an error
//     if (chrome.runtime.lastError) {
//       message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
//     }
//   });
// }
//
// window.onload = scanForContent;
