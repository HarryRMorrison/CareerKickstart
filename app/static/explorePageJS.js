var totalQuestions = 0;

function insertMessages(number, cardTemplate) {
    let $column = $('#messageBoard').children();
    for (let i = 0 ; i < number ; i++){
        let card = $(cardTemplate);
        card.find(".card-title").html('<h6>'+'NewTitle'+'</h6>');
        card.find(".card-subtitle").html('<p> Deloitte </p>');
        card.find(".card-body").val('New Description');
        card.find(".card-action").find('#like').html('<i class="fa fa-thumbs-o-up"></i> '+i);
        card.find(".card-action").find('#comment').html('<i class="fa fa-comments-o"></i> '+i);
        $($column.eq(i%4)).append(card);
    }
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
        if (bottomDistance <= 1000) {
            $.get("/getcard",function(responseText) {
                insertMessages(30, responseText);
            });
        }
    });
});