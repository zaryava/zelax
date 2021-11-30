new Vue({
    el: '#appu',
    data: {
    dus: []
    },
    methods: {
        zarya: function () {
            const vm = this;
            axios.get('/api')
            .then(function (response) {
            vm.dus = response.data
            })
        },
        intervalData: function () {
            setInterval(() => {
                this.zarya();
                }, 10000);
            }
        },
    mounted () {
        // Run the functions once when mounted
        this.zarya();
        // Run the intervalData function once to set the interval time for later refresh
        this.intervalData();
    }
});

new Vue({
    el: '#navapp',
    data: {
    nav: []
    },
    methods: {
        zaryanav: function () {
            const vm = this;
            axios.get('/apin')
            .then(function (response) {
            vm.nav = response.data
            })
        },
        intervalData: function () {
            setInterval(() => {
                this.zaryanav();
                }, 10000);
            }
        },
    mounted () {
        // Run the functions once when mounted
        this.zaryanav();
        // Run the intervalData function once to set the interval time for later refresh
        this.intervalData();
    }
})
