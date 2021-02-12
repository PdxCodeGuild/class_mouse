const content = document.querySelector('#content')
// const url = 'https://favqs.com/api/qotd'
const url = 'https://opentdb.com/api.php'

// fetch(url).then(function (response) {
//     console.log(response)
// })

// axios.get(url).then(function (response) {
//     console.log(response)
// })

let categoryCode = 18

axios({
    method: 'get',
    url: url,
    params: {
        amount: 20,
        category: categoryCode,
        difficulty: 'easy',
        type: 'multiple'
    }
}).then(response => {
    const questions = response.data.results
    console.table(questions)

    for (question of questions) {
        let h3 = document.createElement('h3')
        h3.innerText = question.question
        let answers = question.incorrect_answers
        answers.push(question.correct_answer)
        answers.sort()
        content.appendChild(h3)
        for (answer of answers) {
            let button = document.createElement('button')
            button.innerText = answer
            button.value = answer == question.correct_answer ? true : false
            button.addEventListener('click', function () {
                if (button.value === "true") {
                    button.style.color = 'green'
                } else {
                    button.style.color = 'red'
                }
            })
            content.appendChild(button)
        }

    }

})

