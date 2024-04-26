var totalQuestions = 0;


function insertMessages(number) {
    let $column = $('#messageBoard').children();
    for (let i = 0 ; i < number ; i++){
        $newCard.append($titleCard).append($subCard).append($textCard).append($actionCard);
        $($column.eq(i%5)).append($newCard);
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
    $.get("/getcard",function(data) {
        const cardTemplate = data
    });
    addDropdownFilters();
});

$(document).ready(function() {
    $(window).on('scroll', function() {
        // Calculate the distance from the bottom
        var scrollPosition = $(window).scrollTop() + $(window).height();
        var bottomDistance = $(document).height() - scrollPosition;
      
        // Check if the distance from the bottom is 500px or less
        if (bottomDistance <= 1000) {
            insertMessages(30);
        }
    });
});