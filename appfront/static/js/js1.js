


if(isLoggedIn){
    document.getElementById(' ').innerHTML="person.name"
}

function checkLogForHamkari() {
    if(isLoggedIn){
        open('/farakhan_detail_sherkat/1')
    }
    else{
        document.getElementById('id01').style.display='block'
    }
}



// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
