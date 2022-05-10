import React, { Component } from "react";
import Chart from "react-apexcharts";
import { connect } from "react-redux";
import { getDistribuicao } from "../../middleware/servicesDashboard";
class PieChart extends React.Component {
  constructor(props) {
    super(props);
    console.log("PROPS", this.props);
    this.state = {
      series: [44, 55, 41, 17, 15],
      options: {
        chart: {
          type: "donut",
        },
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200,
              },
              legend: {
                position: "bottom",
              },
            },
          },
        ],
      },
    };
  }

  getData = async () => {
    var dados = await getDistribuicao(localStorage.getItem("id"));

    this.setState({
      series: dados.data.serie,
      options: {
        chart: {
          type: "donut",
        },
        labels: dados.data.labels,
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200,
              },
              legend: {
                position: "bottom",
              },
            },
          },
        ],
      },
    });
  };

  componentDidMount() {
    this.getData();
  }

  render() {
    return (
      <div id="chart">
        <Chart
          options={this.state.options}
          series={this.state.series}
          type="donut"
          width="500"
          height="300"
        />
      </div>
    );
  }
}

export default PieChart;
