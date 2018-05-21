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
    var comment_form = document.getElementById(review_id);
    if (comment_form.style.display == 'none') {
        comment_form.style.display = 'block';
    }
    else {
        comment_form.style.display = 'none'
    }
}

function showReviewForm() {
    var review_form = document.getElementById('reviewForm');
    if (review_form.style.display == 'none') {
        review_form.style.display = 'block';
    }
    else {
        review_form.style.display = 'none'
    }
}
