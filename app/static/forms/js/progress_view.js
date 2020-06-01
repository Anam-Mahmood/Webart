jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});

jQuery(document).ready(function($) {
     var x = document.getElementsByClassName("progress-bar");
     var i;
     for (i = 0; i < x.length; i++) {
           console.log(x[i].style.width);
           if(x[i].style.width =="0%") {
            //$("#done").hide();
           // $("#not_done").show();
            document.getElementById("done").setAttribute("disabled","True");
            break;
        }
        else {
              //$("#not_done").hide();
             // $("#done").show();
             document.getElementById("done").removeAttribute("disabled");
         }
       }

    });
