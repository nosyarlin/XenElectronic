import React from 'react';

export default function Checkout(props) {
    return (
        <div>
            <form>
                <div className="form-group">
                    <label>Billing Address</label>
                    <input className="form-control" id="billingAddress" placeholder="Enter billing address"/>
                </div>
                <div className="form-group">
                    <label >Payment Method</label>
                    <input className="form-control" id="paymentMethod" placeholder="Enter payment method"/>
                </div>
                <button type="submit" className="btn btn-primary">Confirm</button>
            </form>
        </div>
    );
}