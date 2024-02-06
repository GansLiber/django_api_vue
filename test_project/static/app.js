const {createApp, reactive, onMounted} = Vue;

createApp({
    setup() {
        const orders = reactive({data: []});

        onMounted(() => {
            axios.get('/api/orders/')
                .then(function (response) {
                    orders.data = response.data;
                    console.log(orders.data);
                })
                .catch(function (error) {
                    console.error(error);
                });

        });

        return {orders};
    }
}).mount('#orders_app');