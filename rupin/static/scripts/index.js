$(document).ready(function() {
    $("form").submit(function (event) {
        event.preventDefault();

        var formData = {
            email: $("#email").val(),
            password: $("#password").val(),
        };

        var request = $.ajax({
            type: "POST",
            url: "api/v1/sign_in",
            data: formData,
            dataType: "json",
            encode: true,
        });

        request.done(function (data) {
            console.log(data);

        });

        request.fail(function (jqXHR, status) {
            console.log("PISAPOPA");
            $(".help").html(
            '<small id="emailHelp" class="form-text text-muted">'+jqXHR.responseText+'</small>'
            );
        });
    });

    var delay = false;
    var currentPage = 1;
    var pageCount = $(".section").length;
    var form_showed = false;

    $("#login").click( function() {
      $(".form-container").toggle("fast");
      $(".shadow").toggle("fast");

      form_showed = !form_showed;
    });

    $(document).on('mousewheel DOMMouseScroll', function(event) {
        if (delay) return;

        delay = true;
        setTimeout(function() { delay = false }, 400)

        if (form_showed) return;

        var wheelDelta = event.originalEvent.wheelDelta || -event.originalEvent.detail;

        if (wheelDelta < 0) {
            if (currentPage < pageCount) { currentPage++; }
        } else {
            if (1 < currentPage) { currentPage-- }; 
        }
    
        $('html,body').animate({ scrollTop: $('#sec' + currentPage).offset().top }, 50);
    });
});  