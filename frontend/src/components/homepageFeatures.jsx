import React, { Component } from "react";
import FoodInfo from "./foodInfo";

/*
<div className="container-fluid">
          <div className="row row-cols-2 gy-3">
            <div className="col">Wiley</div>
            <div className="col">Win</div>
            <div className="col">Column</div>
            <div className="col">Column</div>
          </div>
        </div>
*/

//Arrow icon designed by Rainbow Designs (supposed to attribute creators from the site I downloaded it from)

class HomepageFeatures extends React.Component {
  state = {};
  render() {
    return (
      <React.Fragment>
        <div
          className="card shadow mb-3 ms-3 me-3 p-3 bg-body"
          style={{ borderRadius: "30px" }}
        >
          <div className="card-body">
            <h5 className="card-title">{this.props.diningHallName}</h5>
            <h6 className="card-subtitle mb-4 text-muted">
              Highest Rated Items...
            </h6>

            <div className="container-fluid">
              <div className="row row-cols-4">
                <div className="col">
                  <FoodInfo />
                </div>
                <div className="col">
                  <FoodInfo />
                </div>
                <div className="col">
                  <FoodInfo />
                </div>
                <div className="col">
                  <div
                    className="card border-secondary"
                    style={{ borderRadius: "30px" }}
                  >
                    <div className="card-body">
                      <img
                        src={"./right-arrow.png"}
                        class="card-img-top"
                        alt="..."
                      />
                      <h6 className="card-text">Full Menu</h6>
                      <p className="card-text">and leave reviews</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default HomepageFeatures;
