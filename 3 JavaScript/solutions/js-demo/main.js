

// sayHello2("Hello Class Mouse")


// This function will be hoisted
function sayHello(message){
    alert(message)
}

// This function is declared in place
let sayHello2 = function(message){
    alert(message)
}

// New hotness
let sayHello3 = (message) => {
    alert(message)
}

// If only one parameter, no parenthesis needed, one line return no '{}' needed 
let sayHello4 = message => alert(message)


let colors = ["blue", "green", "red", "yellow"]

// colors.forEach(color => sayHello(color))