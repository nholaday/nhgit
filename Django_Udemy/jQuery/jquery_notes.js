Do the same thing in jQuery but easier:
// jQuery
vars divs = $('div')
$(el).css('border-width', '20px');
$(document).ready(function(){ //code
})

// Vanilla
var divs = document.querySelectorAll('div')
el.style.borderWidth = '20px';
EventListener


// Grab any item:
var listitems = $('li')
var somep = $('#grabid')
$('.grabclass')

// Change css of an object
listitems.eq(0)  //first element
listitems.eq(0).css('border', '20px red solid')
somep.text("new text")
somep.html("<em>italic</em>")
somep.attr('ref','www.webiste.com') //change an attribute

// Can change the class of an element

// <style>
// .turnRed{
//     background: red;
//     color: white;
// }
// </style>
somep.addClass('turnRed')
somep.removeClass('turnRed')
somep.toggleClass('turnRed')

// Events
$('h1').click(function(){
    console.log('clicked')
})