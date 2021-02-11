// const title = document.querySelector('#title')
// const userInput = document.querySelector('#cc-number')
const buttonsDiv = document.querySelector('#buttons')
const correctGuessesDiv = document.querySelector('#correct-guesses')
const startBtn = document.querySelector('#start-btn')
const hangmanImage = document.querySelector('#hangman-image')


startBtn.addEventListener('click', main)

// console.log(title.innerHTML)
// title.style.color = "blue"
// title.style.fontSize = "4em"
// title.innerText = "Hello World"


// function handleChange(){
//     title.innerText = userInput.value
// }

// userInput.addEventListener('input', handleChange)
async function main(){
    hangmanImage.src = hangman_pics[0]

    while(buttonsDiv.firstChild){
        buttonsDiv.removeChild(buttonsDiv.firstChild)
    }
    while(correctGuessesDiv.firstChild){
        correctGuessesDiv.removeChild(correctGuessesDiv.firstChild)
    }


    const alphabet = "abcdefghijklmnopqrstuvwxyz"
    let remainingGuesses = 6

    for (letter of alphabet){
        const btn = document.createElement('button')
        btn.innerText = letter
        btn.addEventListener('click', function(){
            // console.log(correctGuessesDiv.children)
            if(remainingGuesses > 0){
                btn.disabled = true
                if(selectedWord.includes(btn.innerText)){
                    for(i in selectedWord){
                        if(selectedWord[i] === btn.innerText){
                            correctGuessesDiv.children[i].innerText = btn.innerText
                        }
                    }
                } else {
                    remainingGuesses--
                    hangmanImage.src = hangman_pics[6 - remainingGuesses]
                    btn.style.color = 'red'
                    setTimeout(function(){
                        btn.style.color = 'gray'
                    }, 1000)
                }
            } else {
                for(child of correctGuessesDiv.children){
                    child.style.border = '1px solid red'
                }
            }
        })
        btn.className = 'btn'
        buttonsDiv.appendChild(btn)
    }

    let words = "hello world"
    let data = await axios.get('https://raw.githubusercontent.com/PdxCodeGuild/class_owl/master/1%20Python/data/english.txt')
    
    words = data.data
    
    words = words.split('\n')

    let wordLen = words.length
    let index = Math.floor(Math.random() * wordLen)
    let selectedWord = words[index]
    console.log(selectedWord)

    for(letter of selectedWord){
        let span = document.createElement('span')
        span.innerText = "-"
        span.className = "correct-guesses"
        correctGuessesDiv.appendChild(span)
    }


}


hangman_pics = [
    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Hangman-0.png/60px-Hangman-0.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Hangman-1.png/60px-Hangman-1.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Hangman-2.png/60px-Hangman-2.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Hangman-3.png/60px-Hangman-3.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Hangman-4.png/60px-Hangman-4.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Hangman-5.png/60px-Hangman-5.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Hangman-6.png/60px-Hangman-6.png'
]