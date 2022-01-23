import React, { Component } from "react";

class FoodInfo extends Component {
  constructor(props) {
    super(props);
    console.log("test2");
    console.log(props.data);
  }

  render() {
    return (
      //{this.props.data[0].food ? this.props.data.food : ""}
      <React.Fragment>
        <div className="card border-secondary" style={{ borderRadius: "30px" }}>
          <div className="card-body">
            <img src="" className="card-img-top" alt="..." />
            <h6 className="card-text"></h6>
            <p className="card-text text-muted">average</p>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default FoodInfo;
