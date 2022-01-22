import React, { Component } from 'react';
import HomepageFeatures from './components/homepageFeatures';
import 'bootstrap/dist/css/bootstrap.min.css';

class HomepageDataHandler extends Component {
    state = {
        //temporary for completion purposes
        //will dynamically adjust values
        
    }
    
    render()  {
        return (
            <React.Fragment>
                <h2 className='mb-3 mt-3' style={{ textAlign: 'center' }}>Purdue Dining Hall Menus</h2>

                <div className="container-fluid">
                    <div className="row row-cols-1 gy-3">
                        <div className="col"><HomepageFeatures diningHallName="Wiley" ></HomepageFeatures></div>
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