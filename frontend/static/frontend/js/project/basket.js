$(document).ready(function () {
    var form = $('#basket_form');

    form.on('click', function () {
        alert('123');
        var btn = $('#basket_btn');
        var book_name = btn.data('book_name');
        var book_id = btn.data('book_id');
    })
})