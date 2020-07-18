// $(document)

// The DOM
// DOM is Document Object Model

console.log(document);

// GET vs SET

// var htmlElement = 
// document.getElementById('second').innerHTML = [2, 4, 6, 8];

// var element = document.getElementById('second').innerHTML = [2, 4, 6, 8];
// console.log(typeof(element));

function sayHello(){
    document.getElementById('second').innerHTML = "Hello!";
}


// console.log(htmlElement);

// JQuery Functions

// selector
// $('div')
// $(#second)

// $('#click').click(function(){
//     document.getElementById('second').innerHTML = "Hello!";

// })

// When first block is clicked, third block hide
var yellow = false;

$('#first_block').click(function() {
    $("#third").hide();
    console.log(this, "This is this")
    console.log($(this), "This is $this")
    if(yellow == false){
        $(this).css("background-color", "yellow");
        yellow = true
    } else {
        $(this).css("background-color", "white");
        green = false;
    }
})