let app = new Vue({
    el: '#app',
    data: {
        baseURL: 'https://opentdb.com/api.php',
        amount: "",
        difficulty: '',
        categoryCode: '',
        type: '',
        categories: [],
        questions: []
    },
    methods: {
        getQuiz: async function () {
            const response = await axios({
                method: 'get',
                url: this.baseURL,
                params: {
                    amount: this.amount,
                    category: this.categoryCode,
                    difficulty: this.difficulty,
                    type: this.type,
                }
            })

            let questions = response.data.results
            for (question of questions) {
                this.questions.push({
                    question: question.question,
                    answers: [question.correct_answer].concat(question.incorrect_answers)
                })
            }
        },
        decodeHTML: function (html) {
            const txt = document.createElement('textarea');
            txt.innerHTML = html;
            return txt.value;
        }

    },
    created: async function () {
        const response = await axios({
            method: 'get',
            url: 'https://opentdb.com/api_category.php'
        })
        this.categories = response.data.trivia_categories
    }
})