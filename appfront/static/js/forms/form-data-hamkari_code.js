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
    var form = new FormData();
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
    var national_code = inputNationalCode.value;

    form.append("national_code", national_code);
    form.append("darman", darman);
    form.append("sakht", sakht);
    form.append("amoozesh", amoozesh);
    form.append("farhangi", farhangi);
    form.append("daroo", daroo);
    form.append("lebas", lebas);
    form.append("ghaza", ghaza);
    form.append("tahrir", tahrir);
    form.append("masaleh", masaleh);
    form.append("naghdi_mostaghim", naghdi_mostaghim);
    form.append("naghdi_ghest", naghdi_ghest);

    var settings3 = {
        "async": true,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/api/create_cooperation_code/",
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
    $.ajax(settings3).done(function (response) {
        window.alert('موفقیت همکاری با کد ملی');
        console.log(response)
    });

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
