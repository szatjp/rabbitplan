$(document).ready(function () {
     $(".predou").one('click', function (event) {  
           //event.preventDefault();
           //do something
           $(this).prop('disabled', true);
     });
});