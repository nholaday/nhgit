// Events
$('h1').click(function(){
    console.log($(this).text() + ' was clicked!');
    $('p').eq(1).fadeToggle();
})

// Key Press
$('input').eq(0).keypress(function(){
    $('h3').toggleClass('turnBlue');
})

$('input').eq(0).keypress(function(){
    if (event.which === 13){  // Do something on Enter key
        $('h3').toggleClass('turnRed');
    }
})

// on() acts like AddEventListener
$('p').eq(0).on('dblclick',function(){
    $(this).fadeToggle();
})

// Effects and animations
$('input').eq(1).on('click',function(){
    $('li').eq(2).fadeToggle(2000);
})