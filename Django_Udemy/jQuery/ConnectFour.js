// let p1 = prompt("Player 1 (Blue) enter your name:")
// let p2 = prompt("Player 2 (Red) enter your name:")

let p1 = 'Zandooza'
let p2 = 'Tomompa'
let turn = p1;
let color = "blue"
$('#whichplayer').text(turn + ", it's your turn to lay a " + color + " circle")

let colnum;
let colbuttons;
let row;

function checkWinner(x,y){
    
}


function colclick(){
    // grab the class, this is the same for all buttons in the column
    colnum = $(this).attr('class');
    colbuttons = $('.'+colnum);
    
    // start at the bottom and check if the button is grey
    // if it is, change the color, otherwise move up till you find a grey one
    row = colbuttons.length-1;
    while (row >= 0) {
        if ($(colbuttons).eq(row).css('background-color') === "rgb(128, 128, 128)") {

            if (turn === p1){
                $(colbuttons).eq(row).css('background-color', "rgb(66, 209, 244)");
                turn = p2;
                color = "red";
            } else {
                $(colbuttons).eq(row).css('background-color', "rgb(255, 117, 114)");
                turn = p1;
                color = "blue"
            }
            break;
        };
        row--;
    };
    
    console.log($(this).index())

    $('#whichplayer').text(turn + ", it's your turn to lay a " + color + " circle");
}

// Watching for clicks on any buttons
// for (var j = 0; j < $('button').length; j++) {
//     $('button').eq(j).click(colclick)
// }

let coords = []
let count = 0;
for (var y = 0; y < 7; y++) {
    coords[y] = [];
    for (var x = 0; x < 7; x++) {
        coords[y][x] = $('button').eq(count);
        coords[y][x].click(colclick)
        count++;
    }
}