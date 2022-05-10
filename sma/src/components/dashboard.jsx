import React from "react";
import { connect } from "react-redux";
import "./dashboard.css";
import BarChart from "../components/dashboard/bar";
import LineChart from "../components/dashboard/line";
import PieChart from "../components/dashboard/pie";
import StackedChart from "./dashboard/stacked";
import Navbar from "./navbar";

class Dashboard extends React.Component {
  render() {
    console.log("produtorId(dashboard.jsx): " + this.props.id);
    return (
      <>
        <Navbar />
        <div className="charts-frame-1">
          {/* <BarChart /> */}
          <LineChart />
        </div>
        <div className="charts-frame-1">
          <PieChart />
          <StackedChart />
        </div>
      </>
    );
  }
}

export default Dashboard;
// const mapStateToProps = (state) => ({
//   nome: state.AutenticationReducer.nome,
//   email: state.AutenticationReducer.email,
//   id: state.AutenticationReducer.id,
// });

// export default connect(mapStateToProps, {})(Dashboard);
