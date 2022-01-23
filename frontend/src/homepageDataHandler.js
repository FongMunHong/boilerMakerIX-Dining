import React, { Component } from 'react';
import HomepageFeatures from './components/homepageFeatures';
import 'bootstrap/dist/css/bootstrap.min.css';

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
    state = {
        //temporary for completion purposes
        //will dynamically adjust values
        //wileyData: //this.props.dataItems //.filter(c => c.court.equals("wiley"))
    }
    
    render()  {
        return (
            <React.Fragment>
                <h2 className='mb-3 mt-3' style={{ textAlign: 'center' }}>Purdue Dining Hall Menus</h2>

                <div className="container-fluid">
                    <div className="row row-cols-1 gy-3">
                        <div className="col"><HomepageFeatures diningHallName="Wiley" foodData={this.props.wileyData}></HomepageFeatures></div>
                        <div className="col"><HomepageFeatures diningHallName="Windsor"></HomepageFeatures></div>
                        <div className="col"><HomepageFeatures diningHallName="Ford"></HomepageFeatures></div>
                        <div className="col"><HomepageFeatures diningHallName="Earhart"></HomepageFeatures></div>
                        <div className="col"><HomepageFeatures diningHallName="Hillenbrand"></HomepageFeatures></div>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}

export default HomepageDataHandler;