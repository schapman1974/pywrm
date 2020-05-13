let signalcount = 0;
let conncount = 0;
let globalHold = {};

function signal_template(...args){
    eventnum = -1;
    retevent = this["event"+parseInt(eventnum)]+"_return";
    let widget = window[this.widgetname];
    enc_args = btoa(JSON.stringify(args));
    sendHttpPost("/runfunction?args="+enc_args+"&session_id="+window.name+"&widget_id="+this.widget_id+"&return_event="+retevent);
}

function initmodule(){
    let offset = (new Date()).getTimezoneOffset()/60
    sendHttpPost("/initmodule"+document.location.search+"?session_id="+window.name+"&location="+document.location.href+"&utcoffset="+offset.toString());
}

function escapeRegExp(string) {
    return string.replace(/([.*+?^=!:${}()|\[\]\/\\])/g, "\\$1");
}

function replaceAll(string, find, replace) {
  return string.replace(new RegExp(escapeRegExp(find), 'g'), replace);
}

function sendHttpPost(str_url) {
    let xmlHttpReq = false;
    let self = this;
    
    // Mozilla/Safari/Chrome
    if (window.XMLHttpRequest) {
       xmlHttpReq = new XMLHttpRequest();
    }
    // IE
    else if (window.ActiveXObject) {
        xmlHttpReq = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlHttpReq.open('POST',str_url, true);
    xmlHttpReq.timeout = 0;
    window.conncount+=1;
    xmlHttpReq.onreadystatechange = function() {
        if (this.readyState === 4) {
            handleresult(this.responseText);
            window.conncount-=1;
            this.onreadystatechange = null;
            this.abort();
        }
    }
    xmlHttpReq.send();
}

for (let asigloop = 0; asigloop < 100; asigloop++){
    new_funct_string = replaceAll(signal_template.toString(), "signal_template", "signal" + parseInt(asigloop))
    new_funct_string = replaceAll(new_funct_string, "eventnum = -1", "eventnum = " + parseInt(asigloop))+";"
    eval(new_funct_string);
}

function handleresult(response){
    // This function handles the result when reaching out to the pywrm endpoint
    operations = JSON.parse(response);
    for (i = 0; i < operations.length; i++) {
        operation = operations[i];
        console.log(operation);
        let widget_id = operation["widget_id"];
        let widget_type = operation["widget_type"];
        let widget_set = operation["widget_set"];
        // Handle initialization of a widget
        if (operation["type"] == "init_widget") {
            if (widget_set == "dhx"){
                globalHold[widget_id] = new dhx[widget_type]("maindiv", operation["args"][0]);
            } else if (widget_set == "w2ui"){ 
                $("#maindiv")["w2"+widget_type.toLowerCase()](operation["args"][0]);
                globalHold[widget_id] = w2ui[operation["args"][0]["name"]]
            }
            globalHold[widget_id].widget_id = widget_id;
        // Handle Attach function
        } else if (operation["function_name"] == "attach" || operation["function_name"] == "content"){
            let new_widget_id = operation["kwargs"]["widget_id"];
            if (widget_set == "dhx"){
                globalHold[new_widget_id] = new dhx[widget_type](null, operation["kwargs"]["config"]);
                globalHold[widget_id].cell(operation["kwargs"]["cell_id"]).attach(globalHold[new_widget_id]);
            } else if (widget_set == "w2ui"){
                $()["w2"+widget_type.toLowerCase()](operation["kwargs"]["config"]);
                globalHold[new_widget_id] = w2ui[operation["kwargs"]["config"]["name"]];
                globalHold[widget_id].content(operation["kwargs"]["cell_id"], globalHold[new_widget_id]);
            }
            globalHold[new_widget_id].widget_id = new_widget_id
        } else if (operation["type"] == "function"){
            args = operation["args"];
            globalHold[widget_id][operation["function_name"]](...args);
        } else if (operation["type"] == "cell_function"){
            args = operation["args"];
            if (widget_set == "dhx"){
                globalHold[widget_id].cell(operation["cell_id"])[operation["function_name"]](...args);
            } else if (widget_set == "w2ui"){
                globalHold[widget_id][operation["function_name"]](operation["cell_id"], ...args);
            }
        } else if (operation["type"] == "add_signal"){
            if (widget_set == "dhx"){
                globalHold[widget_id].events.on(operation["function_name"], window["signal" + parseInt(signalcount)]);
            } else if (widget_set == "w2ui"){
                let event = operation["function_name"].slice(2, operation["function_name"].length+1).toLowerCase();
                globalHold[widget_id].on(event, window["signal" + parseInt(signalcount)]);
            }
            globalHold[widget_id]["event" + parseInt(signalcount)] = operation["function_name"];
            signalcount += 1;
        }
      } 
}

function genUniqueID() {
    let d = new Date().getTime();
    let uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        let r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
}