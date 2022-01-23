import React, { Component } from "react";
import Button from "react-bootstrap";

class FullMenuItem extends React.Component {
  /*
    styles = {
    marginTop: 50,
    marginLeft: 50,
    marginRight: 50,
  };
  */
  state = {};
  render() {
    return (
      <React.Fragment>
        <div
          className="card shadow mb-3 ms-3 me-3 p-3"
          style={{ borderRadius: "30px" }}
        >
          <img src="..." className="food-img" alt="img-of-food" />
          <div className="card-body">
            <h5 className="food-name">Food Name</h5>
            <p className="food-rating">
              This will be some sort of rating thing, not a p tag I hope
            </p>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default FullMenuItem;
