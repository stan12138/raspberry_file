var login_btn = document.getElementById("login-button");
if(login_btn){
    login_btn.onclick = ajax_handle_submit;
}
var httprequest;

function ajax_handle_submit(e) {
    var input_user = document.getElementById("user");

    var input_password = document.getElementById("password");

    if(input_user.value==""){
        ;
    }
    else if(input_password.value==""){
        ;
    }
    else{
        var form = document.getElementById("login-form");
        
        var form_data = new FormData(form);
        httprequest = new XMLHttpRequest();
        // httprequest.onreadystatechange = ajax_handle_response;
        httprequest.open("POST", '/login');
        httprequest.send(form_data);
    }
}

function ajax_handle_response() {
    if(httprequest.readyState == 4 && httprequest.status == 200) {
        var change_part = document.getElementById("login-part");
        change_part.innerHTML = httprequest.responseText;
    }

    var logout_btn = document.getElementById("logout-button");
    if(logout_btn){
        logout_btn.onclick = ajax_logout;
    }

    var login_btn = document.getElementById("login-button");
    if(login_btn){
        login_btn.onclick = ajax_handle_submit;
    }
    var register_btn = document.getElementById("register-button");
    if(register_btn){
        register_btn.onclick = register;
    }

}