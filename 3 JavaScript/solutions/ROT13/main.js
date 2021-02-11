const userInput = document.querySelector('#user-input')
const button = document.querySelector('#cypher')
const output = document.querySelector('#output')
const number = document.querySelector('#cypher-amount')


button.addEventListener("click", function() {
    let person = {
        firstName: "Joe",
        lastName: 'Personson'
    }


    let textToEncode = userInput.value.toLowerCase()
    let amount = parseInt(number.value)
    output.innerText = encode(textToEncode, amount) 
    console.warn("this is a warning")
    console.error("this is an error")
    console.table(person)
})

function encode(text, offset){
    const lookUpTable = "abcdefghijklmnopqrstuvwxyz"
    let encodedText = ''
    for(char of text){
        if(lookUpTable.includes(char)){
            let index = (lookUpTable.indexOf(char) + offset) % lookUpTable.length
            encodedText += lookUpTable[index]
        } else {
            encodedText += char
        }
    }
    return encodedText
}