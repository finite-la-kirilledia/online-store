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

$(document).ready(function () {

})

function like(user_id, review_id) {
    $.ajax({
        url: 'like',
        type: 'GET',
        data: {review_id: review_id, user_id: user_id},
        success: [function (data) {
            $.ajax({
                url: 'get_likes_count',
                type: 'GET',
                data: {review_id: review_id},
                success: [function (data) {
                    let likes = document.getElementById('likes' + review_id);
                    likes.innerHTML = '+' + data['likes_count'];
                    $.ajax({
                        url: 'is_liked',
                        type: 'GET',
                        data: {review_id: review_id, user_id: user_id},
                        success: [function (data) {
                            if (data['is_liked'] == true) {
                                document.getElementById('like-btn' + review_id).style.display = 'none';
                                document.getElementById('liked-btn' + review_id).style.display = 'block';
                            }
                            else {
                                document.getElementById('like-btn' + review_id).style.display = 'block';
                                document.getElementById('liked-btn' + review_id).style.display = 'none';
                            }
                        }]
                    })
                }]
            })
        }]
    })
}