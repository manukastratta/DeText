function DOMtoString(document_root) {
    var html = '',
        node = document_root.firstChild;
    while (node) {
        switch (node.nodeType) {
        case Node.ELEMENT_NODE:
            html += node.outerHTML;
            break;
        case Node.TEXT_NODE:
            html += node.nodeValue;
            break;
        case Node.CDATA_SECTION_NODE:
            html += '<![CDATA[' + node.nodeValue + ']]>';
            break;
        case Node.COMMENT_NODE:
            html += '<!--' + node.nodeValue + '-->';
            break;
        case Node.DOCUMENT_TYPE_NODE:
            // (X)HTML documents are identified by public identifiers
            html += "<!DOCTYPE " + node.name + (node.publicId ? ' PUBLIC "' + node.publicId + '"' : '') + (!node.publicId && node.systemId ? ' SYSTEM' : '') + (node.systemId ? ' "' + node.systemId + '"' : '') + '>\n';
            break;
        }
        node = node.nextSibling;
    }
    return html;
}

function writeHelloWorld() {
    document.write('Hello world')
}

var docHTML = DOMtoString(document)
console.log("CONTENT SCRIPT RUNNING")
console.log("http://127.0.0.1:5000/");

$.post("http://127.0.0.1:5000/", {html: docHTML},
    function (response) {
        console.log("IN THE ANONYMOUS FUNCTION");
        console.log("response.trigger is equal to: ");
        console.log(response)
        console.log(response.trigger);
          if (response.trigger == '1') {
              console.log("DISPLAY CONTENT WARNING");
              window.confirm("Warning: this website may contain content related to sexual violence that could be disturbing for some users.");
          } else {
                console.log("do NOT DISPLAY CONTENT WARNING");
                //window.confirm("Warning: this website may contain content related to sexual violence that could be disturbing for some users.");
          }
});



