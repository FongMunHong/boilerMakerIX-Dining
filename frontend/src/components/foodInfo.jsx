import React, { Component } from "react";

class FoodInfo extends Component {
  state = {};
  render() {
    return (
      <React.Fragment>
        <div className="card border-secondary" style={{ borderRadius: "30px" }}>
          <div className="card-body">
            <img src="" className="card-img-top" alt="..." />
            <h6 className="card-text">{}</h6>
            <p className="card-text text-muted">average</p>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default FoodInfo;
