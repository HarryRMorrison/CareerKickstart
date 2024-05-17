function like_adjust(questionid, adjust){
    $.ajax({ 
        url: '/api/likeadjust/?qid='+questionid+'&num='+adjust, 
        type: 'PUT', 
        success: function (result) {
            console.log(adjust)
            if (adjust===1){
                $('#'+questionid).find('.like').html('<i class="fa fa-thumbs-up"></i> '+result.likes)
            }
            else {
                console.log(adjust)
                $('#'+questionid).find('.like').html('<i class="fa fa-thumbs-o-up"></i> '+result.likes)
            }
        } 
    });
    return
}

function a_like_adjust(ans_id, adjust){
    $.ajax({ 
        url: '/api/likeadjust/answer/?ans_id='+ans_id+'&num='+adjust, 
        type: 'PUT', 
        success: function (result) {
            console.log(adjust)
            if (adjust===1){
                $('#'+ans_id).find('.a-like').html('<i class="fa fa-thumbs-up"></i> '+result.likes)
            }
            else {
                console.log(adjust)
                $('#'+ans_id).find('.a-like').html('<i class="fa fa-thumbs-o-up"></i> '+result.likes)
            }
        } 
    });
    return
}


$(document).ready(function() {
    $('.like').click(function(){
        questionid = $(this).closest('.card').attr('id');
        if ($(this).attr('aria-pressed') === "false"){
            like_adjust(questionid, 1);
            $(this).attr('aria-pressed',"true");
        }
        else {
            like_adjust(questionid, -1);
            $(this).attr('aria-pressed',"false");
        }
    })
    $('.a-like').click(function(){
        ans_id = $(this).closest('.card-answer').attr('id');
        if ($(this).attr('aria-pressed') === "false"){
            a_like_adjust(ans_id, 1);
            $(this).attr('aria-pressed',"true");
        }
        else {
            a_like_adjust(ans_id, -1);
            $(this).attr('aria-pressed',"false");
        }
    })
});