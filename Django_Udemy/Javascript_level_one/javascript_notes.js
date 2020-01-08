Inspect -> Console
Then you can type code like in an IDE:
alert("Hello there")

// Strings
"Can put " + "strings together like this"
"example".length
"hello"[0] // indexes strings like python

// Console
console.log("Prepare to die" + "Lorteen") // outputs to the console
prompt("Enter something:")

// Variables
var myName = value;
var example1; // is undefined because it has no value
var ex2 = null; // is defined but is given a null value

// Objects (javascript equivalent to dict)
carInfo = {make:'bmw', model:'525',year:1995}
// key is a string in reference but not the definition
console.log(carInfo['model']) 

// Operators
let y = 2;
y == "2"; // true, converts string to number
y === "2"; // false, also checks that types are equal
y === 2; // true, type and value are equal
null == undefined; //true
NaN == NaN; //false

// If, else
if (60<80){
    console.log('Sixty less than 80')
}else if (70<80){
    console.log('Seventy less')
}else {
    console.log('not less')
}

// while
while (x < 5) {
    console.log(x);
    if (x ===3){
        break;
    }
    x++;
}

// for loop
for (i = 0; i < 5; i++){
    console.log(i)
}

// Ternary Operator
// A 1 line if statement (condition ? ifTrue : else)
console.log(shp==7 ? "Lucky 7!" : `${shp} is a good number`)

// Functions
function nameFun(first, last='Smith'){
    return (first+last); // last name will default to Smith
}

// arrays
fish = ['one', 2, 'red', true]
// 'for of' is useful for arrays
for (type of fish){
    alert(type)
}
// 'for each' can call a function for every element in the array
fish.forEach(alert)

// Objects - like dicts in python
// can put functions in the object!  Refer to itself with 'this.KEY'
var employee = {
  name: "John Smith",
  job: "Programmer",
  hobbies: ["rock climbing", "car washing", "sewing"],
  nameLength: function(){
      console.log(this.name.length)
  }
}
console.dir(employee)
console.log("Can use . " + employee.name + "or [''] " + employee['job'])
for (i in employee){
    console.log(i) // key
    console.log(employee[i]) // value
}

// Document Object Model - DOM
// Converts html of a webpage into a giant Javascript Object
console.dir(document)
