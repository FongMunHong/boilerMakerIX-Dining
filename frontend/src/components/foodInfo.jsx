import React, { Component } from "react";

class FoodInfo extends Component {
  state = {};
  render() {
    return (
      <React.Fragment>
        <div className="card border-secondary" style={{ borderRadius: "30px" }}>
          <div className="card-body">
            <img src="" class="card-img-top" alt="..." />
            <h6 className="card-text">Popcorn Shrimp</h6>
            <p className="card-text">3.2</p>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default FoodInfo;
