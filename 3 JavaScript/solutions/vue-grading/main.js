let app = new Vue({
    el: '#app',
    data: {
        numberGrade: 0,
        letterGrade: ''
    },
    methods: {
        calcGrade: function () {
            let grade = parseInt(this.numberGrade)
            if (grade > 110) {
                this.sayHello()
            }
            if (grade >= 90) {
                this.letterGrade = "A"
            } else if (grade >= 80) {
                this.letterGrade = "B"
            } else if (grade >= 70) {
                this.letterGrade = "C"
            } else if (grade >= 60) {
                this.letterGrade = "D"
            } else if (grade >= 0) {
                this.letterGrade = "F"
            } else {
                this.letterGrade = "Invalid grade"
            }
        },
        sayHello: function () {
            alert("Are you sure?")
        }
    }
})