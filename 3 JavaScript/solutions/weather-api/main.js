let app = new Vue({
    el: "#app",
    data: {
        loading: true,
        lat: '',
        lon: '',
        sunset: '',
        sunrise: '',
        currentTime: '',
        temp: '',
        iconId: '',
        description: ''
    },
    methods: {

    },
    created: async function () {
        let ip
        let response = await axios({
            method: 'get',
            url: 'https://api.ipify.org',
            params: {
                format: 'json'
            }
        })
        ip = response.data.ip
        response = await axios({
            method: 'get',
            url: 'https://geo.ipify.org/api/v1',
            params: {
                apiKey: IPIFY_API_KEY,
                ipAddress: ip
            }
        })
        this.lat = response.data.location.lat
        this.lon = response.data.location.lng
    },
    watch: {
        lat: async function () {
            let response = await axios({
                method: 'get',
                url: 'https://api.openweathermap.org/data/2.5/onecall',
                params: {
                    lat: this.lat,
                    lon: this.lon,
                    exclude: 'hourly,daily,minutely',
                    appid: WEATHER_API_KEY,
                    units: 'imperial'
                }
            })
            console.log(response);
            this.sunrise = new Date(response.data.current.sunrise * 1000)
            this.sunset = new Date(response.data.current.sunset * 1000)
            this.currentTime = new Date(response.data.current.dt * 1000)
            this.temp = response.data.current.temp
            this.description = response.data.current.weather[0].description
            this.iconId = response.data.current.weather[0].id
            this.loading = false
        }
    }
})