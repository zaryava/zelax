let elem = document.getElementById('ipone').innerHTML;
let index = String(elem)
let url = '/api/' + index;
new Vue({
    el: '#appu',
    data: {
    dus: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/')
        .then(function (response) {
        vm.dus = response.data
        })
    }

})