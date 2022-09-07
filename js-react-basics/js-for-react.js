// Functions with parameters

function add(x, y){
    return x+y
}
console.log(add( 10, 20))  //30
console.log(add( 4, 5 )) //9

// Default parameters

function add( x=0, y=0 ){
    return x+y
}
console.log(add( 10 ))  //20
console.log(add( 4, 5 )) //9

// Objects
const  userryan ={
    name: 'ryan',
   lastname: 'Serra',
    age: 30,
    address: {
        country:'colombia',
        city: 'medellin'
    },
    active: false,
    sendMail: function () {
        return 'sending email….'
    },
    sendMail () {
        return 'sending email….'
    }
}

console.log(userryan)
console.log(userryan.name)  //ryan
console.log(userryan.address.city)  //bogota
console.log(userryan.active)  //false


// Shorthand properties
const product_name= 'laptop'
const product_price= 3000

const newProduct = {
    product_price, // use  just one name
    product_name: product_name,
}
console.log(newProduct)


// Manipulating DOM, event handlers
const titleh1 = document.createElement('h1')
titleh1.innerText = 'Hello world from js'

const button1 = document.createElement('button')
button1.innerText = 'click me'
// events
button1.addEventListener('click', function () {
    console.log('you clicked the button');
    titleh1.innerText = 'Updated h1 title text'
    alert('Hi, title changed')  // pops-up an alert
})

document.body.append(titleh1)
document.body.append(button1)


//---Objects as parameters [28:15]
const userJoe = {
    name: 'joe',
    age: 30
}

function printInfo(user) {
    return '<h1>Hola' + user.name + '</h1>'
}
// console.log(printInfo(user));
document.body.innerHTML = printInfo(user)


//  --- Destructuring
function printInfo( { name }) {
    return '<h1>Hola' + name + '</h1>'
}
function printInfoDes( user) {
    let { name, age } = user
    return '<h1>Hola' + name +', '+ age + '</h1>'
}
// console.log(printInfoDes(user));


// --- Anon functions
const buttonAnon = document.createElement('button')
buttonAnon.innerText = 'click me'

button1.addEventListener( 'click', function(){
    alert('clicked')
} )
document.body.append(buttonAnon)


// ---Arrow functions
const addArrow = (x, y) => {
    return x + y
}
// --Inline arrow functions
const showText = () => 'Inline arrow function'
const showNumber = () => 22
const showBoolean = () => true
const showArray = () => [1,2,3]

const showObject = () => ({ name: 'victor' })

console.log(showText());
console.log(showObject());


//--- Return in functions
//--conditional return 
const buttonret = document.createElement('button')
buttonret.innerText = 'click me'

const isAuthorized = true

buttonret.addEventListener( 'click', () => {
    /* if ( isAuthorized ){
        alert('Authorized')
    } else {
        alert('Not authorized')
    } */
    if ( isAuthorized ){
        return alert('Authorized')
    }
    alert('Not authorized')
    
} )
document.body.append(buttonret)

// --- String literals
const BtnBg = 'yellow'
const Btncolor = 'white'
const Boolcolor = true

// const BtnStyle = `Background: ${BtnBg} , Button: ${Btncolor}`
buttonret.style = `Background: ${BtnBg} , Button: ${Btncolor}`
buttonret.style = `Background: ${Boolcolor ? 'blue': 'red'} , 
Button: ${Btncolor}`

// ---Array methods
const friends = ['Ryan','Masha','Camille']

friendas.array.forEach( (friend) => {
    console.log(friend);
});

// --Map: goes over the array and creates a new array
const newFriends = friends.map(
    function(friend){
        return `Hola ${friend}`
    }
)

console.log(friends);
console.log(newFriends);
// --Find: finds an element and returns it
const findFriends = friends.find(function(friend){
    if (friend === 'Masha')
        return friend
})

// Filter: creates a new array, but filters by any condition
const filterFriend = friends.filter( function(friend){
    if ( friend === 'Ryan' )
        return friend // ['Ryan']
} )
console.log(filterFriend);

const concatFriends = [1,2,3]
console.log( concatFriends.cancat(filterFriend) );
[1,2,3,'Ryan','Masha','Camille']

// --- Spread operator: ...variable
const spreadUser = {
    name: 'John',
    lastname: 'ray'
}
const spreadAddress = {
    street: 'main street 123',
    city: 'bogota'
}

const userInfo = {
    ...user,
    ...address
}
console.log(userInfo);


// --- Modules
// import {function} from './address.js'

console.log(person.location?.city);

// Async/Await
// Fetch(url) - Promises
const ul = document.createElement('ul')


    .then( function(response){
        return response.json()
        // console.log(response);
    }).then( function(data){
        console.log(data);
        data.forEach( function (){
            const li = document.createElement('li')
            li.innerText = post.title
            ul.append(li)
        })
        document.body.append(ul)

    } )

async function loadData(){
    const response = await fetch('https://jsonplaceholder.typicode.com/posts')
    const data = await response.json()
    console.log(data);

    data.forEach( function (){
        const li = document.createElement('li')
        li.innerText = post.title
        ul.append(li)
    })
    document.body.append(ul)

}
loadData()
