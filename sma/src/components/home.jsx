import React, { Component } from "react";
import Navbar from "./navbar";
import colheita from "../assets/images/colheita.jpg";
import "./home.css";
export default class Home extends Component {
  render() {
    return (
      <>
        <div className="body">
          <Navbar />
          <h1 className="title-body">Agricultura Familiar</h1>
          <div className="principal-body-container">
            <img className="img-principal" src={colheita} alt=""/>
          </div>
        </div>
      </>
    );
  }
}