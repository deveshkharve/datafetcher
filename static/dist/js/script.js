$(function() {
    $('#side-menu').metisMenu();
});

//Loads the correct sidebar on window load,
//collapses the sidebar on window resize.
// Sets the min-height of #page-wrapper to window size
$(function() {
    $(window).bind("load resize", function() {
        var topOffset = 50;
        var width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            $('div.navbar-collapse').addClass('collapse');
            topOffset = 100; // 2-row-menu
        } else {
            $('div.navbar-collapse').removeClass('collapse');
        }

        var height = ((this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height) - 1;
        height = height - topOffset;
        if (height < 1) height = 1;
        if (height > topOffset) {
            $("#page-wrapper").css("min-height", (height) + "px");
        }
    });

    var url = window.location;
    // var element = $('ul.nav a').filter(function() {
    //     return this.href == url;
    // }).addClass('active').parent().parent().addClass('in').parent();
    var element = $('ul.nav a').filter(function() {
        return this.href == url;
    }).addClass('active').parent();

    while (true) {
        if (element.is('li')) {
            element = element.parent().addClass('in').parent();
        } else {
            break;
        }
    }
});


/* Function for Forwading form */
function showHideForward(forwardCheckbox) {
    var dispForward = document.getElementById("forwardForm");
    dispForward.style.display = forwardCheckbox.checked ? "block" : "none";
    dispForward.addClass = forwardCheckbox.checked ? "panel-default" : "panel-info";
    var qtyEl = document.getElementById('quantity');
    if( qtyEl.value == '' ){
        qtyEl.value=1
    }

    if(!forwardCheckbox.checked) resetFwdQuote()
}

/* Function for CHA form */
function showHideCha(chaCheckbox) {
    var dispCha = document.getElementById("chaForm");
    dispCha.style.display = chaCheckbox.checked ? "block" : "none";

    document.getElementById('Forwarder').value='Viraje Cargo Care Pvt Ltd'
    document.getElementById('cha').value='Impex Clearing Services Pvt Ltd'
    // check if fwd checked
    if(document.getElementById('chaCheckbox').checked){

        document.getElementById('fromPlace-CHA').value= document.getElementById('originPlace').value

        document.getElementById('cha_commodity').value=document.getElementById('fwd_commodity').value
        document.getElementById('cha_shipper').value = document.getElementById('shipperName').value
        document.getElementById('cha_commodity').value=document.getElementById('fwd_commodity').value


    }

    if (!chaCheckbox.checked) resetCHAQuote()
}

/* Function for Transportation form */
function showHideTransport(transportCheckbox) {
    var dispTransport = document.getElementById("transportForm");
    dispTransport.style.display = transportCheckbox.checked ? "block" : "none";
}

$(document).ready(function() {
    $("#forwardCheckbox").click(function() {
        $(".panel-fwd").toggleClass("panel-primary");
    });
    $("#chaCheckbox").click(function() {
        $(".panel-cha").toggleClass("panel-primary");
    });
    $("#transportCheckbox").click(function() {
        $(".panel-transport").toggleClass("panel-primary");
    });
});

$(function() {
    $('.input-group.date').datepicker({
        autoclose: true,
        clearBtn: true,
        format: "dd/mm/yyyy",
        startDate: "today",
        todayHighlight: true
    });
});

/*$('.input-group.date').datepicker({
    autoclose: true,
    clearBtn: true,
    format: "dd/mm/yyyy",
    startDate: "today",
    todayHighlight: true
});
*/