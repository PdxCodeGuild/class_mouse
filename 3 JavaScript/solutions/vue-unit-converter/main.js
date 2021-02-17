let app = new Vue({
    el: '#app',
    data: {
        units: ['feet', 'meter', 'kilometer', 'yard', 'mile', 'inch'],
        startingUnit: '',
        endingUnit: '',
        outputDistance: 0,
        inputDistance: '',
        gif_url: ''
    },
    methods: {
        convert: async function () {
            const conversion = {
                feet: 0.3048,
                mile: 1609.34,
                meter: 1,
                kilometer: 1000,
                yard: 0.9144,
                inch: 0.0254,
            }

            let inputDistance = parseInt(this.inputDistance)

            let meters = inputDistance * conversion[this.startingUnit]

            this.outputDistance = meters / conversion[this.endingUnit]

            let response = await axios({
                url: 'https://api.giphy.com/v1/gifs/random',
                method: 'get',
                params: {
                    api_key: API_KEY,
                    rating: 'g'
                }
            })
            console.log(response.data.data.images.original_mp4)
            this.gif_url = response.data.data.images.original_mp4.mp4
        }
    }
})