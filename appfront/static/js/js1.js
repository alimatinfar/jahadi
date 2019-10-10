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


if (isLoggedIn) {
    document.getElementById(' ').innerHTML = "person.name"
}

function checkLogForHamkari() {
    if (isLoggedIn) {
        debugger;
        var form = new FormData();

        form.append("profile", id_profile);
        form.append("farakhan", id_farakhan);
        alert(id_profile)
        alert(id_farakhan)

        var settings3 = {
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
            "data": form
        }
        $.ajax(settings3).done(function (response) {
            window.alert('نام شما در لیست افراد آماده برای این فراخوان ثبت شد!');
            console.log(response)
        });
    } else {
        document.getElementById('id01').style.display = 'block'
    }
}


// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
