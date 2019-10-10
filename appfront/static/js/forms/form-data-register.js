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

function validate(event) {

    if ($('form').valid()) {
        debugger;
        var username = inputUsername.value;
        var password = inputPassword.value;

        // var first_name = inputFirstName.value;
        // var last_name = inputLastName.value;
        // var picture = inputPicture.value;
        // var national_code = inputNationalCode.value;
        // var date_birth = inputDateBirth.value;
        // var gender = select_gender.value;
        // var marital = select_marital.value;
        // var father_name = inputFatherName.value;
        // var address = inputAddress.value;
        // var mobile = inputMobile.value;
        // var email = inputEmail.value;

        var form = new FormData();
        form.append("username", username);
        form.append("password", password);
        form.append("last_name", "matinfar");
        form.append("national_code", "0440680743");
        form.append("date_birth", "2000-11-11");
        form.append("gender", "m");
        form.append("address", "sldkjfslkdfjskldfj");
        form.append("mobile", "09195922298");
        form.append("father_name", "masood");
        form.append("email", "alimatinafr1376@gmail.com");
        form.append("password", "201747matin");
        form.append("first_name", "ali");
        form.append("marital", "s");

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "http://127.0.0.1:8000/api/create_user2/",
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
            window.alert('موفقیت یوزر و پروفایل');
            console.log(response)
            event.preventDefault()
            // loadDoc2(response.id);
        });
    }

}

//
// $(document).ready(function () {
//
//     $("form").submit(function (e) {
//         e.preventDefault();//برای اینکه صفحه بعد از سابمیت رفرش نشود!!!!!
//         var u = inputUsername.value;
//         if (username_list.includes(u)) {
//             alert('این نام کاربری قبلا ثبت شده است !!!!!!!!!!!!!!!!!!')
//         } else {
//             validate();
//         }
//     });
//
// });
