var pages = 1;
var isLoading = false;

function getQuestions(){
    search = window.location.href.split("?");
    if (search.length > 1) {
        search = search[1];
    }
    else (
        search = ''
    )
    $.get("/api/explore/?page=" + pages + "&" + search, function(responseText) {
        insertMessages(responseText);
    });
    return 
}

function getDropdownFilters(){
    $.get("/api/filter-retrieve", function(responseText) {
        insertDropdownFilters(responseText);
    });
    return 
}

function insertMessages(newQuestions) {
    let $column = $('#messageBoard').children();
    for (let i = 0 ; i < 28 ; i++){
        if (newQuestions[i]===undefined) {
            return
        }
        let post = newQuestions[i];
        let $newCard = $('<div id="'+post.question_id+'" class="card">');
        let $titleCard = $('<div class="card-title">').html('<h6>'+post.title+'</h6>');
        let $subCard = $('<div class="card-subtitle d-flex">');
        post.tags.forEach(tag => {
            $subCard.append($('<p>').text(tag));
        });
        let $textCard = $('<div class="card-body">').html('<p class="card-text">'+post.description+'</p>');
        let $actionCard = $('<div class="card-action d-flex">').html('<button class="like" aria-pressed="false" type="button"><i class="fa fa-thumbs-o-up"></i>'+post.likes+'</button><button aria-pressed="false" type="button"><i class="fa fa-comments-o"></i>'+post.comments+'</button>');
        let $userinfo = $('<div class="user-info d-flex align-items-center justify-content-center">').html('<img class="profil-pic" src="/static/'+post.profile_pic+'" style="height: 30px; width: 30px; border-radius: 30px;"><b class="d-inline-block text-truncate" style="max-width: 100px;"> '+post.user+' </b><i class="ms-2"> '+post.date+' </i>')
        $actionCard.append($userinfo)
        $newCard.append($titleCard).append($subCard).append($textCard).append($actionCard);
        $($column.eq(i%4)).append($newCard);
        isLoading = false;
    }
    return
}


function insertDropdownFilters(filters) {
    for (let x in filters) {
        let $newFilters = $('<ul class="dropdown-menu" aria-labelledby="' + x + 'Dropdown"></ul>'); 
        for (let i = 0; i < filters[x].length; i++) {
            let filterName = filters[x][i];
            $newFilters.append('<li><a class="dropdown-item"><label><input type="checkbox" name="  ' + filterName + ' ">  ' + filterName + '</label></a></li>');
        }
        $('#' + x + 'Dropdown').after($newFilters);
        console.log('#' + x + 'Dropdown')
    }
}
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

$(window).on("load", function() { 
    getDropdownFilters();
});

$(document).ready(function() {
    $(window).on('scroll', function() {
        // Calculate the distance from the bottom
        var scrollPosition = $(window).scrollTop() + $(window).height();
        var bottomDistance = $(document).height() - scrollPosition;
      
        // Check if the distance from the bottom is 1000px or less
        if (bottomDistance <= 1000 && isLoading == false) {
            isLoading = true;
            getQuestions();
            pages += 1;
        }
    });
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