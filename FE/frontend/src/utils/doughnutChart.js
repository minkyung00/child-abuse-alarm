import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

import { Doughnut } from "vue-chartjs/legacy";
export default {
  extends: Doughnut,
  props: ["chartData", "options"],
  mounted () {
    this.renderChart(this.chartData, this.options);
  }
}