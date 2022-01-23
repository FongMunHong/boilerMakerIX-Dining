import React, { Component } from 'react';
import WileyFeatures from './components/wileyFeatures';
import EarhartFeatures from './components/earhartFeatures';
import FordFeatures from './components/fordFeatures'
import TheGatheringPlaceFeatures from './components/theGatheringPlaceFeatures'
import 'bootstrap/dist/css/bootstrap.min.css';
//import FoodInfo from './components/foodInfo'

/*
{this.props.wileyData.map(data => {
    return (
        
    )
})}



{this.props.foodData.map((data) => {
    return (
    <div key={data.id}>
        <p>{data.id}</p>
        <p>{data.date}</p>
        <p>{data.court}</p>
        <p>{data.food}</p>
        <p>{data.meal_time}</p>
        <p>{data.ratings}</p>
        <p>{data.picture}</p>
    </div>
    );
})}
*/

class HomepageDataHandler extends Component {
    /*
    state = {
        //temporary for completion purposes
        //will dynamically adjust values
        foodData: this.props.wileyData //.filter(c => c.court.equals("wiley"))
    }
    */

    constructor(props) {
      super(props);

      console.log(props);
    //   this.setState = {
    //    foodData: this.props.wileyData
    //   };

      //this.render = this.render.bind(this);
   }
    
    render()  {
        return (
            <React.Fragment>
                <h2 className='mb-3 mt-3' style={{ textAlign: 'center' }}>Purdue Dining Hall Menus</h2>

                <div className="container-fluid">
                    <div className="row row-cols-1 gy-3">
                        <div className="col"><WileyFeatures diningHallName="Wiley" foodData={this.props.wileyData}></WileyFeatures></div>
                        <div className="col"><EarhartFeatures diningHallName="Earhart" foodData={<div></div>}></EarhartFeatures></div>
                        <div className="col"><FordFeatures diningHallName="Ford" foodData={<div></div>}></FordFeatures></div>
                        <div className="col"><TheGatheringPlaceFeatures diningHallName="Hillenbrand" foodData={<div></div>}></TheGatheringPlaceFeatures></div>
                    </div>
                </div>

        
            </React.Fragment>
        );
    }
}

export default HomepageDataHandler;