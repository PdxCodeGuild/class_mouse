let header = document.querySelector('#header')
let input = document.querySelector('#userInput')
let button = document.querySelector('#changeHeader')
let colorPicker = document.querySelector('#colorPicker')
let imageBox = document.querySelector('#imageBox')
let imageHeader = document.querySelector('#image')

let counter = 400

header.style = "color: red;"
header.style.fontSize = "4em"
// console.log(header.innerText)

button.addEventListener('click', function(){
    // alert(input.value)
    header.innerText = input.value
})

header.addEventListener('click', function(){
    header.style.color = colorPicker.value
})

imageHeader.addEventListener('click', () => {
    imageHeader.style.display = 'none'
    counter++
    while(imageBox.firstChild){
        imageBox.removeChild(imageBox.firstChild)
    }
    let image = document.createElement('img')
    image.src = `https://picsum.photos/${counter}`
    image.style.width = '400px'

    image.addEventListener('click', () => {
        image.classList.toggle('animate')
    })


    imageBox.appendChild(image)
})