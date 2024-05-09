var pages = 1;
var isLoading = false;
var tracker = 28;

function getQuestions(){
    $.get("/explore/" + pages, function(responseText) {
        insertMessages(responseText);
    });
    return 
}

function insertMessages(newQuestions) {
    let $column = $('#messageBoard').children();
    for (let i = 0 ; i < 28 ; i++){
        let post = newQuestions[i];
        let $newCard = $('<div class="card">');
        let $titleCard = $('<div class="card-title">').html('<h6>'+post.title+'</h6>');
        let $subCard = $('<div class="card-subtitle d-flex">');
        post.tags.forEach(tag => {
            $subCard.append($('<p>').text(tag));
        });
        let $textCard = $('<div class="card-body">').html('<p class="card-text">'+post.description+'</p>');
        let $actionCard = $('<div class="card-action d-flex">').html('<button id="like" type="button"><i class="fa fa-thumbs-o-up"></i>'+post.likes+'</button><button id="comment" type="button"><i class="fa fa-comments-o"></i>'+post.comments+'</button>');
        $newCard.append($titleCard).append($subCard).append($textCard).append($actionCard);
        $($column.eq(i%4)).append($newCard);
        tracker += 1;
        console.log([tracker, i%4])
        isLoading = false;
    }
    return
}


function addDropdownFilters() {
    for (let x in filters) {
        let $newFilters = $('<ul class="dropdown-menu" aria-labelledby="' + x + '"></ul>'); 
        for (let i = 0; i < filters[x].length; i++) {
            let filterName = filters[x][i];
            $newFilters.append('<li><a class="dropdown-item"><label><input type="checkbox" name="  ' + filterName + ' ">  ' + filterName + '</label></a></li>');
        }
        $('#' + x).after($newFilters);
    }
}

$(window).on("load", function() { 
    addDropdownFilters();
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
});