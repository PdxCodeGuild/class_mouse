let app = new Vue({
    methods: {
        getWeather: function () {

        }
    },
    data: {
        loading: true,
        lat: '',
        lon: ''
    },
    created: function () {
        navigator.geolocation.getCurrentPosition(position => {
            this.lat = position.coords.latitude
            this.lon = position.coords.longitude
        })

        setTimeout(this.getWeather(), 1000)
    },
    watch: {
        lat: function () {
            console.log(this.lat, this.lon);
            this.loading = false
        },
    },
    el: '#app',
})