// Using the DOM and querySelector find something in the webpage
var headOne = document.querySelector('#one')
var headTwo = document.querySelector('#two')
var headThree = document.querySelector('#three')

//To add a mouse over event
headOne.addEventListener('mouseover', function(){
    headOne.textContent = "Mouse Currently Over";
    headOne.style.color = 'red';
})

headOne.addEventListener('mouseout',function(){
    headOne.textContent = "Hover over me";
    headOne.style.color = 'black';
})

headTwo.addEventListener('click',function(){
    headTwo.textContent = 'Clicked on!';
    headTwo.style.color = 'blue';
})

headThree.addEventListener('dblclick',function(){
    headThree.textContent = 'Double Clicked!';
    headThree.style.color = 'purple';
})