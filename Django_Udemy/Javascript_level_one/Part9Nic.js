let first = prompt("Enter your First Name");
let last = prompt("Enter your Last Name");
let age = prompt("Enter your age");
let height = prompt("Enter height");
let pet = prompt("Pet name");

console.log(first[0] + last[0] + age + height + pet[-1]);

if (first[0] == last[0] && 
    (20 < age && age < 30) && 
    170 <= height && 
    pet[pet.length-1] == 'y') {
    console.log("Welcome fine sir to the spy society");
}else {
    console.log("Nothing to see here, move along, move along");
}
