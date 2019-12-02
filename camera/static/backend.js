var pitch_add = document.getElementById("pitch_button_1");
var pitch_decrease = document.getElementById("pitch_button_2")

var yaw_add = document.getElementById("yaw_button_1")
var yaw_decrease = document.getElementById("yaw_button_2")

var httprequest;



if(pitch_add){
    pitch_add.onclick = ajax_pitch_add;
}

if(pitch_decrease){
    pitch_decrease.onclick = ajax_pitch_decrease;
}

if(yaw_add){
    yaw_add.onclick = ajax_yaw_add;
}
if(yaw_decrease){
    yaw_decrease.onclick = ajax_yaw_decrease;
}

function ajax_pitch_add(e) {
    httprequest = new XMLHttpRequest();
    httprequest.onreadystatechange = ajax_handle_response;
    httprequest.open("GET", '/pitch_add', true);
    httprequest.send();
}

function ajax_pitch_decrease(e) {
    httprequest = new XMLHttpRequest();
    httprequest.onreadystatechange = ajax_handle_response;
    httprequest.open("GET", '/pitch_decrease', true);
    httprequest.send();
}

function ajax_yaw_add(e) {
    httprequest = new XMLHttpRequest();
    httprequest.onreadystatechange = ajax_handle_response;
    httprequest.open("GET", '/yaw_add', true);
    httprequest.send();
}

function ajax_yaw_decrease(e) {
    httprequest = new XMLHttpRequest();
    httprequest.onreadystatechange = ajax_handle_response;
    httprequest.open("GET", '/yaw_decrease', true);
    httprequest.send();
}

function ajax_handle_response() {
    ;

}