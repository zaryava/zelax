new Vuen({
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
                }, 5000);
            }
        },
    mounted () {
        // Run the functions once when mounted
        this.zaryanav();
        // Run the intervalData function once to set the interval time for later refresh
        this.intervalData();
    }
})