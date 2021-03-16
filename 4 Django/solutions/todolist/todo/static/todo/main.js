let app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        message: 'Hello from Vue',
        todos: [],
        priorities: [],
        text_input: '',
        priority_input: '',
        sorted: false,
    },
    methods: {
        getTodos: async function () {
            let response = await axios({
                method: 'get',
                url: 'todos/'
            })
            this.todos = response.data
        },
        getPriorities: async function () {
            let response = await axios({
                method: 'get',
                url: 'priorities/'
            })
            this.priorities = response.data
        },
        saveTodo: async function () {
            const csrftoken = Cookies.get('csrftoken')
            response = await axios({
                method: 'post',
                url: 'save_todo/',
                headers: {
                    'X-CSRFToken': csrftoken
                },
                data: {
                    todoText: this.text_input,
                    priorityID: this.priority_input
                }
            })
            this.text_input = ''
            this.priority_input = ''
            if (response.data.message === 'ok') {
                this.getTodos()
            }
        },
        completeTodo: async function (id) {
            await axios({
                method: 'get',
                url: `complete_todo/?todo_id=${id}`
            })
            this.getTodos()
        },
        deleteTodo: async function (id) {
            await axios({
                method: 'get',
                url: `delete_todo/?todo_id=${id}`
            })
            this.getTodos()
        },
        sort: function () {
            if (!this.sorted) {
                this.sorted = true
                this.todos.sort((a, b) => {
                    if (a.text < b.text) return -1
                    if (a.text > b.text) return 1
                    return 0
                })
            } else {
                this.sorted = false
                this.todos.sort((a, b) => {
                    if (a.text > b.text) return -1
                    if (a.text < b.text) return 1
                    return 0
                })
            }
        }
    },
    created: function () {
        this.getTodos()
        this.getPriorities()
    }
})