// Document Object Model
// Changes html of website into a Javascript Object that you can manipulate

Here are some important document attributes:

document.URL -- This is the actual URL of the website
document.body -- This is everything inside of the body
document.head -- This is everything in the head of the page
documnet.links -- These are all the links on the page


Then we also have methods we can use to grab HTML elements:

document.getElementById() -- Returns the element with the id
document.getElementsByClassName() -- Returns list of all elements belonging to a class
document.getElementsByTagName() -- Returns list of all elements with the tag
//querySelector can do what the 'get' functions do but you just put # for id or . for class
document.querySelector() -- Returns the first object matching the CSS style selector
document.querySelectorAll() -- Returns all objects matchin the CSS style selector

// So to change li's with id='pickme' on a page you can do:
pick = document.querySelector('#pickme')
pick.style.color = blue
pick.textContent = "You done been picked"

// You can use these methods to change things:
myvariable.textContent - This returns just the text
myvariable.innerHTML - This returns the actual html
myvariable.getAttribute() - This returns the original attribute
myvariable.setAttribute() - This allowed you to set an attribute

// You can nest querySelectors to drill down to portions of HTML
var special = document.querySelector('#specialid')
var specialp = special.querySelector('a') // anchor tag in special
specialp.getAttribute('href')
specialp.setAttribute('href','https://www.vods.co')

// Event listeners
special.addEventListener('click',function(){
    special.style.color = 'red';
})
