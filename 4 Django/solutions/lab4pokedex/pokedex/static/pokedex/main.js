let index = new Vue({
    el: '#index',
    delimiters: ['[[', ']]'],
    data: {
        message: 'Pokemon!',
        pokemon: '',
    },
    methods: {

    },
    created: async function () {
        let response = await axios({
            method: 'get',
            url: 'api/'
        })
        this.pokemon = response.data.data
    }
})

let detail = new Vue({
    el: '#detail',
    delimiters: ['[[', ']]'],
    data: {
        message: 'Hello World',
        mon: ''
    },
    created: async function () {
        let path = window.location.pathname
        let number = path.split('/')[2]
        let response = await axios({
            method: 'get',
            url: 'api/'
        })
        this.mon = response.data
    }
})