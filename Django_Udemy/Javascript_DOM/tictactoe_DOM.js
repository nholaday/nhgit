var button = document.querySelector('#rst');
var cells = document.querySelectorAll('td');

function restart(){
    for (var i = 0; i < cells.length; i++) {
        cells[i].textContent = '';
    }
}
button.addEventListener('click',restart)

function clickbox(){
    if (this.textContent === '') {
        this.textContent = 'X';
    } else if (this.textContent === 'X') {
        this.textContent = 'O';
    } else {
        this.textContent = '';
    }
}

// cells[0].addEventListener('click',function(){ clickbox(cells[0]); });
// cells[1].addEventListener('click',function(){ clickbox(cells[1]); });

// Doing with Vanilla Javascript
for (var i = 0; i < cells.length; i++) {
    cells[i].addEventListener('click',clickbox);
}

// Doing with jquery
// function clickboxjq(){
//     if ($(this).text() === '') {
//         $(this).fadeIn();
//         $(this).text('X');
//     } else if ($(this).text() === 'X') {
//         $(this).text('O');
//     } else {
//         $(this).fadeOut();
//         $(this).show();
//     }
// }
// $(document).ready(function(){
//     $("td").eq(0).click(clickboxjq);
// });
