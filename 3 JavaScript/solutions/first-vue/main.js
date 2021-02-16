let app = new Vue({
    el: '#app',
    data: {
        message: "Hello Class",
        cool_pic: "https://picsum.photos/200",
        disabled_button: false,
        super_heroes: [
            "Wonder Woman",
            "Wolverine",
            "Howard the Duck",
            "Superman"
        ],
        userInput: ""
    },
    methods: {
        updateHeader: function () {
            this.message = this.userInput
            this.super_heroes.push("Spiderman")
        }
    },
    created: function () {
        this.message = "Some other message"
    }
})