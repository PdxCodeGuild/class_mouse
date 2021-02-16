let app = new Vue({
    el: '#todoApp',
    data: {
        userInput: '',
        priority: 'low',
        todos: [{
            title: "walk the dog",
            priority: "medium"
        }]
    },
    methods: {
        addTodo: function () {
            this.todos.push({
                title: this.userInput,
                priority: this.priority
            })
            this.userInput = ""
            this.priority = "low"
        },
        removeTodo: function (i) {
            this.todos.splice(i, 1)
        }
    },
    created: function () {

    }
})