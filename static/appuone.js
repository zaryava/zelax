let elem = document.getElementById('primer').innerHTML;
let url = '/api/' + elem

new Vue({
  el: '#app',
  data: {
    items: [],
  },
  methods: {
    loadData: function () {
        const vm = this;
        axios.get('/api/10.1.11.206')
        .then(function (response) {
        vm.items = response.items
      });
    }
  })

