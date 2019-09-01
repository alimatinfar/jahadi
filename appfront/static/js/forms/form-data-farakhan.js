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


function getprofile(value) {
    $.each(value, function (index, field) {
        console.log(value)

        let opt = $('<option/>', {
            value: field.id,

            title: field.id,
            text: field.first_name + " " + field.last_name,
        });


        let opt2 = $('<option/>', {
            value: field.id,

            title: field.id,
            text: field.first_name + " " + field.last_name,
        });
        $('select#select_present').append(opt);
        $('select#select_ready').append(opt2);
    });
}


function loadDoc() {


    var hamkari_title = inputHamkariTitle.value;
    var hamkari_type = select_hamkari.value;
    var date_first = inputDatefirst.value;
    var date_end = inputDateEnd.value;
    var place = inputPlace.value;

    var form = new FormData();
    form.append("date_first", date_first);
    form.append("date_end", date_end);
    form.append("place", place);
    form.append("hamkari_title", hamkari_title);
    form.append("hamkari_type", hamkari_type);


    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://127.0.0.1:8000/api/create_farakhan/",
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
        window.alert('موفقیت فراخوان');
        console.log(response)
        loadDoc2(response.id);
        loadDoc3(response.id)
    });


    function loadDoc2(id_farakhan) {

        var s = $('#select_ready').val();

        for (i = 0; i < s.length; i++) {

            var profile = s[i];

            var form2 = new FormData();
            form2.append("profile", profile);
            form2.append("farakhan", id_farakhan);

            var settings2 = {
                "async": true,
                "crossDomain": true,
                "url": "http://127.0.0.1:8000/api/create_profile_ready/",
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
                window.alert('موفقیت پروفایل آماده');
                console.log(response);
            });

        }
    }

    function loadDoc3(id_farakhan) {

        var s = $('#select_present').val();

        for (i = 0; i < s.length; i++) {

            var profile = s[i];

            var form3 = new FormData();
            form3.append("profile", profile);
            form3.append("farakhan", id_farakhan);

            var settings3 = {
                "async": true,
                "crossDomain": true,
                "url": "http://127.0.0.1:8000/api/create_profile_present/",
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
                window.alert('موفقیت پروفایل حاضر');
                console.log(response)
            });
        }
    }


}


$(document).ready(function () {

    $("form").submit(function (e) {
        e.preventDefault();//برای اینکه صفحه بعد از سابمیت رفرش نشود!!!!!
        loadDoc();
    });

});

myAjax("/api/create_profile/", getprofile, 'GET')