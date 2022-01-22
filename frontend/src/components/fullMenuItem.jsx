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
        <div class="card">
          <img src="..." class="food-img" alt="img-of-food" />
          <div class="card-body">
            <h5 class="food-name">Food Name</h5>
            <p class="food-rating">
              This will be some sort of rating thing, not a p tag I hope
            </p>
          </div>
        </div>

        <div class="card">
          <img src="..." class="card-img-start" alt="..." />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </p>
            <a href="#" class="btn btn-primary">
              Go somewhere
            </a>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default FullMenuItem;
