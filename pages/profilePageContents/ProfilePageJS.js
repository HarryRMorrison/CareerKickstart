// Function declaration for display_random_image
function display_random_image() 
{
    // Array containing image objects with src, width, and height properties
    var theImages = [{
        src: "http://farm4.staticflickr.com/3691/11268502654_f28f05966c_m.jpg",
        width: "240",
        height: "160"
    }, {
        src: "http://farm1.staticflickr.com/33/45336904_1aef569b30_n.jpg",
        width: "320",
        height: "195"
    }, {
        src: "http://farm6.staticflickr.com/5211/5384592886_80a512e2c9.jpg",
        width: "500",
        height: "343"
    }];
    
    // Array to hold pre-buffered images
    var preBuffer = [];
    // Loop to preload images
    for (var i = 0, j = theImages.length; i < j; i++) {
        preBuffer[i] = new Image();
        preBuffer[i].src = theImages[i].src;
        preBuffer[i].width = theImages[i].width;
        preBuffer[i].height = theImages[i].height;
    }
   
    // Function to generate random integer between min and max values
    function getRandomInt(min,max) 
    {
        // Generating random integer between min and max
        imn = Math.floor(Math.random() * (max - min + 1)) + min;
        // Returning the pre-buffered image corresponding to the random index
        return preBuffer[imn];
    }  

    // Getting a random image from preBuffer array
    var newImage = getRandomInt(0, preBuffer.length - 1);
 
    // Removing any previous images
    var images = document.getElementsByTagName('img');
    var l = images.length;
    for (var p = 0; p < l; p++) {
        images[0].parentNode.removeChild(images[0]);
    }
    // Displaying the new image  
    document.body.appendChild(newImage);
}