function showComments(review_id) {
    var comments_div = document.getElementById(review_id);
    if (comments_div.style.display == 'none') {
        comments_div.style.display = 'block';
    }
    else {
        comments_div.style.display = 'none'
    }
}

function showCommentForm(review_id) {
    var comments_form = document.getElementById(review_id);
    if (comments_form.style.display == 'none') {
        comments_form.style.display = 'block';
    }
    else {
        comments_form.style.display = 'none'
    }
}

