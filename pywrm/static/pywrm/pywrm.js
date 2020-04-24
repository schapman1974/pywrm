var signalcount = 0;
var conncount = 0;
var globalHold = {};

function signal_template(...args){
    asignum = 1;
    var widget = window[this.widgetname];
    sendHttpPost("/runfunction?args="+btoa(JSON.stringify(args))+"&uid="+window.name+"&widget="+widget.id);
}

function addsignal(){
    eval(replaceAll(signal_template.toString(), "signal_template", "signal" + parseInt(signalcount+1)));
    signalcount = signalcount + 1;
}

function initmodule(){
    var offset = (new Date()).getTimezoneOffset()/60
    sendHttpPost("/initmodule"+document.location.search+"?uid="+window.name+"&location="+document.location.href+"&utcoffset="+offset.toString());
}

function sendHttpPost(str_url) {
    var xmlHttpReq = false;
    var self = this;
    
    // Mozilla/Safari/Chrome
    if (window.XMLHttpRequest) {
       var xmlHttpReq = new XMLHttpRequest();
    }
    // IE
    else if (window.ActiveXObject) {
        var xmlHttpReq = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlHttpReq.open('POST',str_url, true);
    xmlHttpReq.timeout = 0;
    window.conncount+=1;
    xmlHttpReq.onreadystatechange = function() {
        if (this.readyState == 4) {
            handleresult(this.responseText);
            window.conncount-=1;
            this.onreadystatechange = null;
            this.abort();
        }
    }
    xmlHttpReq.send();
}

function handleresult(response){
    console.log("handle-result3");
    operations = JSON.parse(response);
    for (i = 0; i < operations.length; i++) {
        operation = operations[i];
        console.log(operation);
        if (operation[0] == "init_widget") {
            globalHold[operation[1]] = new dhx.Layout(operation[1], operation[2]);
        } else if (operation[0] == "attach"){
            globalHold[operation[3]] = new dhx.Layout(null, operation[4]);
            globalHold[operation[1]].cell(operation[2]).attach(globalHold[operation[3]]);
        }
      } 
    JSON.parse(response);
}

function genUniqueID() {
    var d = new Date().getTime();
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
}