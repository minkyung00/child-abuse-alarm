<template>
  <div>
    <b-card>
      <b-card-title>
        <img src="https://www.kakaocorp.com/page/ico_stock.png" width="36" height="36" alt="" class="ico_cate">  이번 주
      </b-card-title>
      <b-card-text>
        <DoughnutChart
          ref="doghnutChart"
          :chartData="chart.data"
          :weeklyData="weeklyData"
          :chartOptions="chart.options"
          id="chart-container"
        />
        <ul class="chart-description">
          <!-- <h5 class="chart-title">{{ `이번주 폭력행위 횟수` }}</h5> -->

          <li class="chart-legend">
            <div class="chart-legend__info">
              <div class="chart-legend__label">
                <b-badge
                  pill
                  variant="danger"
                  class="badge-danger"
                >{{ `위험` }}</b-badge>
                <p class="percent">
                  {{ `${this.weeklyData.percentDanger}%` }}
                </p>
              </div>
              <p class="total">
                {{ `총 ${this.weeklyData.total_danger}회` }}
              </p>
            </div>
          </li>
          
          <li class="chart-legend">
            <div class="chart-legend__info">
              <div class="chart-legend__label">
                <b-badge
                  pill
                  variant="danger"
                  class="badge-warning"
                >{{ `경고` }}</b-badge>
                <p class="percent">
                  {{ `${this.weeklyData.percentWarning}%` }}
                </p>
                
              </div>
              <p class="total">
                {{`총 ${this.weeklyData.total_warning}회`}}
              </p>
            </div>
          </li>

          <li class="chart-legend">
            <div class="chart-legend__info">
              <div class="chart-legend__label">
                <b-badge
                  pill
                  variant="danger"
                  class="badge-caution"
                >{{ `주의` }}</b-badge>
                <p class="percent">
                  {{ `${this.weeklyData.percentCaution}%` }}
                </p>
              </div>
              <p class="total">
                {{`총 ${this.weeklyData.total_caution}회`}}
              </p>
            </div>
          </li>

          <p class="legend-description">
            * 위험: 5회 이상의 폭력행위,&nbsp;
            경고: 2회 ~ 4회 폭력행위,&nbsp;
            주의: 1회 폭력행위
          </p>
        </ul>
      </b-card-text>
      <button
        class="detail-button"
        @click="handleRoute"
      >상세히 보러가기</button>
    </b-card>
  </div>
</template>

<script>
import DoughnutChart from "@/utils/doughnutChart.js"
export default {
  name: "weeklyDataDoughnutChart",
  components: {
    DoughnutChart
  },
  props: {
    weeklyData: Object
  },
  data () {
    return {
      chart: {
        data: {
          labels: ["위험", "경고", "주의"],
          datasets: [{
            data: [],
            backgroundColor: [
              "#f96f7d",
              "#ffcc80",
              "#ffba94"
            ],
            borderWidth: 2,
            hoverOffset: 4,
          }]
        },
        options: {
          plugins: {
            title: {
              display: true,
              text: '이번 주 강도별 폭력행위'
            },
            legend: {
              display: true,
              position: "bottom",
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
              layout: {
                padding: 20
              },
              responsive: false,
              maintainAspectRatio: false,
            }
          }
        }
      },
    }
  },
  methods: {
    handleRoute () {
      this.$router.push({
        name: 'Weekly'
      })
    },
  }
}
</script>

<style lang="scss" scoped>
.card-text {
  @media (max-width: $break-small) {
    display: block !important;
  }
}

#chart-container {
  // position: relative;
  // width: 70%;
  // height: 70%;
  width: 70%;
  height: 70%;
  min-width: 300px;
  min-height: 300px;
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
      margin: 1rem 0;
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
      @media (max-width: $break-xlarge) {
        display: none;
      }
      @media (max-width: $break-large) {
        display: block;
      }
    }

    .total {
      flex-shrink: 0;
      font-size: calc(0.75rem + 0.7vw);
    }
  }
  .legend-description {
    font-size: 12px;
    color: $color-grey-500;
  }
}

.badge {
  padding: 0.5em 1.2em;
  margin: 0 1rem;
}

.detail-button {
  float: right;
  background-color: transparent;
  color: $color-nav-green;
  &:hover {
    background-color: $color-grey-50;
  }
}
</style>