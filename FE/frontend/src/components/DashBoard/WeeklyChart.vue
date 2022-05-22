<template>
  <div>
    <b-card>
      <b-card-title>
        <img src="https://www.kakaocorp.com/page/ico_stock.png" width="36" height="36" alt="" class="ico_cate">  이번 주
      </b-card-title>
      <b-card-text>
        <DoughnutChart
          ref="weeklyChart"
          :chartData="chart.data"
          :options="chart.options"
          id="chart-container"
        />
        <div class="chart-description">
          <h5 class="chart-title">{{ `이번주 폭력행위 횟수` }}</h5>

          <div class="chart-legend">
            <div class="chart-legend__info">
              <div class="chart-legend__label">
                <b-badge
                  pill
                  variant="danger"
                  class="hit-badge"
                >{{ `때리기` }}</b-badge>
                <p class="percent">70%</p>
              </div>
              <p class="total">총 7회</p>
            </div>
          </div>
          
          <div class="chart-legend">
            <div class="chart-legend__info">
              <div class="chart-legend__label">
                <b-badge
                  pill
                  variant="danger"
                  class="kick-badge"
                >{{ `밀치기` }}</b-badge>
                <p class="percent">30%</p>
              </div>
              <p class="total">총 3회</p>
            </div>
          </div>
        </div>
      </b-card-text>
      <button class="detail-button">상세히 보러가기</button>
    </b-card>
  </div>
</template>

<script>
import DoughnutChart from "@/utils/chart.js"
export default {
  name: "WeeklyChart",
  components: {
    DoughnutChart
  },
  data () {
    return {
      chart: {
        type: 'doughnut',
        data: {
          labels: ["때리기", "밀치기"],
          datasets: [{
            backgroundColor: [
              "rgba(255, 99, 132)",
              "rgb(255, 205, 86)"
            ],
            // borderColor: [
            //   "rgba(255, 99, 132, 1)",
            //   "rgba(255, 159, 64, 1)"
            // ],
            borderWidth: 1,
            hoverOffset: 4,
            data: [70, 30]
          }]
        },
        options: {
          plugins: {
            legend: {
              display: false,
              position: "right",
              labels: {
                font: {
                  size: 16
                }
              },
              tooltip: {
                boxWidth: 15,
                bodyFont: {
                  size: 16
                }
              },
              responsive: false,
              maintainAspectRatio: false,
            }
          }
        }
      },
    }
  }
}
</script>

<style lang="scss" scoped>
#chart-container {
  position: relative;
  width: 300px;
  height: 300px;
}

.chart-description {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  padding: 1rem 1.5rem;


  .chart-title {
    margin-bottom: 40px;
  }

  .chart-legend {
    // margin: 1.5rem 0;

    &::after {
      content: '';
      display: block;
      height: 1px;
      margin: 1.5rem 0;
      background-color: $color-grey-300;
    }

    .chart-legend__info {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .chart-legend__label {
      display: flex;
      align-items: center;
    }

    p {
      margin: 0;
      font-weight: $font-weight-semibold;
    }

    .percent {
      font-size: 18px;
    }

    .total {
      font-size: 20px;
    }
  }
}



.badge {
  padding: 0.5em 2em;
  margin: 0 1.5rem;
  border-radius: 1rem;
  color: white;
  font-size: calc(0.5rem + 0.4vw);
}

.kick-badge {
  background-color: $color-text-warning;
}

.hit-badge {
  background-color: $color-text-danger;
}

.detail-button {
  float: right;
  background-color: transparent;
  color: $color-nav-green;
}
</style>