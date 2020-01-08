function main() {
    let roster = [];
    let input

    while (input != "quit") {
        input = prompt("Choose between: add, remove, display, quit");
        
        if (input == "add"){
            roster = addName(roster);
        } else if (input == "display") {
            display(roster);
        } else if (input == "remove") {
            roster = remove(roster);
        }
    }
}

function addName(roster) {
    roster.push(prompt("Enter a new name to add to the roster"));
    console.log(roster);
    return roster;
}

function display(roster){
    console.log(roster);
}

function remove(roster){
    let remname = prompt("Remove what name?");
    let index = roster.indexOf(remname);
    console.log("index is " + index);
    if (index > -1) {
        roster.splice(index,1);
    }
    return roster;
}


main()
