import secret_key_decorator from "../local_settings.js"

export default {
    delimiters: ["{$", "$}"],
    data() {
        return {
            chartData: null,
            loading: false,
        }
    },
    mounted() {
        this.loading = true
        extraeUrl(urlApi)
            .then((resp) => {
                this.chartData = resp
                this.renderChart()
            })
        .catch((error) => {
            console.error(error)
        })
        .finally(() => {
            this.loading = false
        })
    },
    methods: {
        renderChart() {
            let tmpltMyChart = this.$refs.myChart.getContext("2d")
            const myChart = new Chart(tmpltMyChart, {
                type: "bar",
                data: this.chartData,
            })
        },
    },
    template: await extraeUrl(urlHtmlGrafico).then((resp) => {
        return resp
    }),
}

async function extraeUrl(url) {
    let respuesta = await axios.get(url, {
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-MyApp-Secret-Key": secret_key_decorator,
        },
    })
    let external_template = await respuesta.data
    return external_template
}
