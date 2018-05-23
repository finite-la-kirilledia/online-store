$(document).ready(function () {
    var form = $('#basket_form');

    form.on('submit', function (event) {
        event.preventDefault();
        var basket_btn = $('#basket_btn');
        var book_id = basket_btn.data('book_id');
        var user_id = basket_btn.data('user_id');

        var data = {};
        data.book_id = book_id;
        data.user_id = user_id;

        var csrf_token = $('#basket_form [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");

        $.ajax({
            url: url,
            type: 'PUT',
            data: data,
            success: [function (data) {
            }],
            error: function () {
                console.log("error")
            }
        })
    });

    $(function () {
        $('[data-toggle="popover"]').popover()

    })
    $('.popover-dismiss').popover({
        trigger: 'focus'
    })


})