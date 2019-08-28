function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
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

function loadDoc() {
    debugger;
    var username = inputUsername.value;
    var password = inputPassword.value;

    var form = new FormData();
    form.append("username", username);
    form.append("password", password);


    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/api/create_user/",
        "method": "POST",
        dataType: "JSON",
        "headers": {
            "X-CSRFToken": getCookie('csrftoken'),
            "User-Agent": "PostmanRuntime/7.11.0",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Postman-Token": "f34ecd63-f5af-4cde-8bcd-f876cff98a7c,de157247-7ca8-4c47-a13a-ad88a89d72c1",
            "Host": "127.0.0.1:8000",
            // "cookie": "csrftoken=tBUqeCLo7rLqQqzYAlH3IVsz7kOPBrMXtZ01eAnlgcwtOThVhLQMTBnbb2bJUah9",
            "accept-encoding": "gzip, deflate",
            "content-length": "521",
            "Connection": "keep-alive",
            "cache-control": "no-cache"
        },
        "processData": false,
        "contentType": false,
        "mimeType": "multipart/form-data",
        "data": form
    }
    $.ajax(settings).done(function (response) {
        window.alert('موفقیت یوزر');
        console.log(response)
        loadDoc2(response.id);
    });

    function loadDoc2(id_user) {

        var first_name = inputFirstName.value;
        var last_name = inputLastName.value;
        var picture = inputPicture.value;
        var national_code = inputNationalCode.value;
        var date_birth = inputDateBirth.value;
        var gender = select_gender.value;
        var father_name = inputFatherName.value;
        var address = inputAddress.value;
        var mobile = inputMobile.value;

        var form2 = new FormData();
        form2.append("user", id_user);
        form2.append("first_name", first_name);
        form2.append("last_name", last_name);
        form2.append("national_code", national_code);
        form2.append("date_birth", date_birth);
        form2.append("gender", gender);
        form2.append("address", address);
        form2.append("mobile", mobile);
        form2.append("picture", picture);
        form2.append("father_name", father_name);

        var settings2 = {
            "async": true,
            "crossDomain": true,
            "url": "http://127.0.0.1:8000/api/create_profile/",
            "method": "POST",
            dataType: "JSON",
            "headers": {
                "X-CSRFToken": getCookie('csrftoken'),
                "User-Agent": "PostmanRuntime/7.11.0",
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Postman-Token": "f34ecd63-f5af-4cde-8bcd-f876cff98a7c,de157247-7ca8-4c47-a13a-ad88a89d72c1",
                "Host": "127.0.0.1:8000",
                // "cookie": "csrftoken=tBUqeCLo7rLqQqzYAlH3IVsz7kOPBrMXtZ01eAnlgcwtOThVhLQMTBnbb2bJUah9",
                "accept-encoding": "gzip, deflate",
                "content-length": "521",
                "Connection": "keep-alive",
                "cache-control": "no-cache"
            },
            "processData": false,
            "contentType": false,
            "mimeType": "multipart/form-data",
            "data": form2
        }
        $.ajax(settings2).done(function (response) {
            window.alert('موفقیت پروفایل');
            console.log(response);
            loadDoc3(response.id)
        });
    }

    function loadDoc3(id_profile) {

        var form3 = new FormData();
        var naghdi_mostaghim = inputmostaghim.checked;
        var naghdi_ghest = inputghest.checked;
        var daroo = inputdaroo.checked;
        var lebas = inputlebas.checked;
        var ghaza = inputghaza.checked;
        var tahrir = inputtahrir.checked;
        var masaleh = inputmasaleh.checked;
        var darman = inputdarman.checked;
        var sakht = inputsakht.checked;
        var amoozesh = inputamoozesh.checked;
        var farhangi = inputfarhangi.checked;

        form3.append("profile", id_profile);
        form3.append("darman", darman);
        form3.append("sakht", sakht);
        form3.append("amoozesh", amoozesh);
        form3.append("farhangi", farhangi);
        form3.append("daroo", daroo);
        form3.append("lebas", lebas);
        form3.append("ghaza", ghaza);
        form3.append("tahrir", tahrir);
        form3.append("masaleh", masaleh);
        form3.append("naghdi_mostaghim", naghdi_mostaghim);
        form3.append("naghdi_ghest", naghdi_ghest);

        var settings3 = {
            "async": true,
            "crossDomain": true,
            "url": "http://127.0.0.1:8000/api/create_cooperation/",
            "method": "POST",
            dataType: "JSON",
            "headers": {
                "X-CSRFToken": getCookie('csrftoken'),
                "User-Agent": "PostmanRuntime/7.11.0",
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Postman-Token": "f34ecd63-f5af-4cde-8bcd-f876cff98a7c,de157247-7ca8-4c47-a13a-ad88a89d72c1",
                "Host": "127.0.0.1:8000",
                // "cookie": "csrftoken=tBUqeCLo7rLqQqzYAlH3IVsz7kOPBrMXtZ01eAnlgcwtOThVhLQMTBnbb2bJUah9",
                "accept-encoding": "gzip, deflate",
                "content-length": "521",
                "Connection": "keep-alive",
                "cache-control": "no-cache"
            },
            "processData": false,
            "contentType": false,
            "mimeType": "multipart/form-data",
            "data": form3
        }
        $.ajax(settings3).done(function (response) {
            window.alert('موفقیت همکاری');
            console.log(response)
        });
    }
}

$(document).ready(function () {

    $("#inputnaghdi").click(function () {//حالت فعال کردن نقدی !!!!
        if ($(this).is(':checked')) {
            $("#inputmostaghim").prop('disabled', false);
            $("#inputghest").prop('disabled', false);
            $("#inputmostaghim").prop('checked', true);
        } else {
            $('#inputmostaghim').prop('checked', false);
            $('#inputghest').prop('checked', false);
            $("#inputmostaghim").prop('disabled', true);
            $("#inputghest").prop('disabled', true);

        }
    });


    $("form").submit(function (e) {
        e.preventDefault();//برای اینکه صفحه بعد از سابمیت رفرش نشود!!!!!
        loadDoc();
    });

});
