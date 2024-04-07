/*
In the future:
- Change from img to actual request
- make request a function containing the number of likes and the top comment

<div class="card">
    <img src="forest.jpg" class="card-img-top">
</div>

<ul class="dropdown-menu" 
                aria-labelledby="multiSelectDropdown"> 
                <li> 
                  <label> 
                    <input type="checkbox" 
                           value="Java"> 
                        Java 
                    </label> 
                </li> 
                <li> 
                  <label> 
                    <input type="checkbox" 
                           value="C++"> 
                        C++ 
                    </label> 
                </li> 
                <li> 
                  <label> 
                    <input type="checkbox" 
                           value="Python"> 
                        Python 
                    </label> 
                </li> 
            </ul> 

*/


let messagesLoaded = 0;
const images = ['20180714_201544', '4', '5', 'forest', 'IMG_0206', 'IMG_5481', 'jager-2', 'n02085782_2162', 'n02086240_5140', 'n02086910_2579', 'n02087394_9520', 'n02088238_11318', 'n02089973_3480', 'n02090722_001', 'n02090722_002', 'n02091032_1360', 'n02092002_1646', 'n02092002_3', 'n02092339_2006', 'n02092339_7403', 'n02093428_3353', 'n02093647_2626', 'n02095314_3039', 'n02095889_293', 'n02096051_6332', 'n02096177_4505', 'n02096294_836', 'n02097130_2416', 'n02097130_2821', 'n02097130_572', 'n02097298_4126', 'n02097474_4404', 'n02098105_1199', 'n02098105_95', 'n02099429_3194', 'n02100236_4295', 'n02100583_2465', 'n02101006_2031', 'n02102480_5452', 'n02102973_3344', 'n02102973_4510', 'n02105505_4351', 'n02105855_13090', 'n02106166_204', 'n02106166_2345', 'n02106550_8166', 'n02107908_1235', 'n02109525_13780', 'n02109961_6221', 'n02110063_18180', 'n02110627_13014', 'n02110806_5343', 'n02112137_10176', 'n02112350_7219', 'n02113023_3840', 'n02113186_12499', 'n02113624_4589', 'n02113978_471', 'n02115913_2414', 'WhatsApp_Image_2022-08-06_at_4.48.38_PM'];
const filters = {'companyDropdown':['KPMG','Deloitte','EY','PwC'],'roleDropdown':['Internship','Graduate'],'disciplineDropdown':['Comp Science','Finance','Marketing','Engineering'],'industryDropdown':['KPMG','Deloitte','EY','PwC']}

function getMessages(number) {
    let cut = images.slice(messagesLoaded,messagesLoaded+number);
    let out = [];
    for (let img in cut){
        console.log(cut[img]);
        out.push("./test/"+cut[img]+".jpg");
    }
    messagesLoaded += number;
    return out
}

function insertMessages(number) {
    let names = getMessages(number);
    for (let i = 0 ; i < number ; i++) {
        let $newCard = $('<div class="card">'); 
        $newCard.html('<img src="'+names[i]+'" class="card-img-top img-fluid">'); 
        $('#messageBoard').append($newCard);
    }
}


function addDropdownFilters() {
    for (let x in filters) {
        let $newFilters = $('<ul class="dropdown-menu" aria-labelledby="' + x + '"></ul>'); 
        for (let i = 0; i < filters[x].length; i++) {
            let filterName = filters[x][i];
            $newFilters.append('<li><a class="dropdown-item"><label><input type="checkbox" name="  ' + filterName + ' ">' + filterName + '</label></a></li>');
        }
        $('#' + x).after($newFilters);
    }
}



$(window).on("load", function() { 
    insertMessages(30);
    addDropdownFilters();
});

$(document).ready(function () { 

}); 
