$(document).ready( function () {
    $('#navbar-menu').hide();
    $('#property_type_open').fadeOut(-1);
    setTimeout( function() {
        document.getElementById('bg-load').style.bottom = "100%";
        document.getElementById('bg-load').style.transition = 'bottom 5s';
        $("#img-load").fadeOut(4000);
    }, 5);


});

function open_menu() {
$('#navbar-menu').fadeIn(500);
$('#td-navbar-function').html('<i class="fa fa-times" onclick="close_menu();"></i> Close');
document.getElementsByClassName('navbar')[0].style.position = 'sticky';
}

function close_menu() {
$('#navbar-menu').fadeOut(500);
$('#td-navbar-function').html('<i class="fa fa-bars" onclick="open_menu();"></i> Menu');
document.getElementsByClassName('navbar')[0].style.position = 'relative';
}

function property_type_open() {
$('#property_type_open').fadeIn(500);
}

function property_type_close() {
$('#property_type_open').fadeOut(500);
var ele = document.getElementsByName('p_type');
for (i=0; i < ele.length; i++) {
    if (ele[i].checked) {
        document.getElementById('property_type').value = ele[i].value;
    }
}
}

var httpRequest = new XMLHttpRequest();

function message() {
    document.getElementsByClassName('loader')[0].style.display = 'inline';

    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var subject = document.getElementById('subject').value;
    var message = document.getElementById('message').value;

    httpRequest.onreadystatechange = writeContent;
	httpRequest.open('POST', '/mailer');
	httpRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
				
	httpRequest.send("name="+name+"&email="+email+"&subject="+subject+"&message"+message);

    function writeContent() {
	    if(httpRequest.readyState === 4) {
	        if(httpRequest.status == 200) {
                setTimeout( function() {
                    document.getElementsByClassName('loader')[0].style.display = 'none';
                    document.getElementById('fafacheck').style.display = 'inline';
                }, 2000);
            
                setTimeout( function() { 
                    $('#fafacheck').fadeOut(500);
                    document.getElementById('name').value = '';
                    document.getElementById('email').value = '';
                    document.getElementById('subject').value = '';
                    document.getElementById('message').value = '';
                }, 3000);
                
		    }
		    else {
		    	alert("Error!!. Check your internet connection");
		    	document.getElementsByClassName("loader")[0].style.display = "None";
      	    }
		}
		else {
			// response not ready yet
		}
	}
}