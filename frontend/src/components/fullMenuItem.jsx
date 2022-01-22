import React, { Component } from 'react';
import Button from 'react-bootstrap';




class FullMenuItem extends React.Component {
    styles = {
        marginTop: 50,
        marginLeft: 50,
        marginRight: 50
    }
    state = {};
    render() { 
        return(
            <React.Fragment>
                <div class="card" style={this.styles}>
                <img src="..." class="food-img" alt="img-of-food"/>
                    <div class="card-body">
                        <h5 class="food-name">Food Name</h5>
                        <p class="food-rating">This will be some sort of rating thing, not a p tag I hope</p>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}
 
export default FullMenuItem;