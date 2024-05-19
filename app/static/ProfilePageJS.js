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

var imageArray = [
    { 
      //address URL of the image
      src: "female1.png",
      //size for the image to be display on webpage
    }, 
    {
      src: "female2.png",
    },
    {
      src: "female3.png",
    }, 
    {
      src: "male1.png",
    }, 
    {
      src: "male2.png",
    }, 
    {
      src: "male3.png",
     } ];

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
    });
    $('.card-body').click(function(){
        qid =  $(this).closest('.card').attr('id');
        window.location.href = "/question/"+qid;
    });
    $('.card-title').click(function(){
        qid =  $(this).closest('.card').attr('id');
        window.location.href = "/question/"+qid;
    })
    $('.comment').click(function(){
        qid =  $(this).closest('.card').attr('id');
        window.location.href = "/question/"+qid;
    })
});