function setCookie(cname, cvalue, exdays) {
    debugger;
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}


function myAjax(url, resultFunction = null, method = 'GET', errorMessage = 'error') {
    let ajax = $.ajax({
        url,
        type: method,
        "headers": {
            "Authorization": "Token " + getCookie('Token'),
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "cache-control": "no-cache",
            'Access-Control-Allow-Origin': '*',


        },
        error: function (err) {
            console.log("error in request is:", errorMessage);
        }
    });
    ajax.then(function (value) {
        if (resultFunction) resultFunction(value);
    });
}

function validate(event) {

    debugger;
    var username = inputUserName.value;
    var password = inputPassword.value;

    var form = new FormData();
    form.append("username", username);
    form.append("password", password);


    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/api/login/",
        "method": "POST",
        dataType: "JSON",
        "headers": {
            "User-Agent": "PostmanRuntime/7.11.0",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Postman-Token": "473ce5c2-470a-4153-b55b-fc498a40d197,f9cae697-093c-457b-af0d-27b4979323c9",
            "Host": "127.0.0.1:8000",
            "accept-encoding": "gzip, deflate",
            "content-length": "284",
            "Connection": "keep-alive",
            "cache-control": "no-cache"
        },
        "processData": false,
        "contentType": false,
        "mimeType": "multipart/form-data",
        "data": form
    };

    $.ajax(settings).done(function (response) {


        tokenid = response.token;
        tokenname = 'Token';

        alert(tokenid)
        setCookie(tokenname, tokenid, 60);

        console.log(response);
        debugger;
    });
}

