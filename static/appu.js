let elem = document.getElementById('primer').innerHTML;
let url = '/api/' + elem
new Vue({
    el: '#appu',
    data: {
    dus: []
    },
    created: function () {
        const vm = this;
        axios.get(url)
        .then(function (response) {
        vm.dus = response.data
        })
    }

})