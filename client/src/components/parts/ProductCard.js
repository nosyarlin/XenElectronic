import React from 'react';

export default function ProductCard(props) {

    var currency_formatter = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'SGD',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
    });

    return (
        <div className="col-sm-6 col-lg-4">
            <div className="card mx-1 mt-4">
                <div className="card-body">
                    <h5 className="card-title">{props.name}</h5>
                    <p className="card-text">{currency_formatter.format(props.price)}</p>
                    <button
                        className="btn btn-primary"
                        onClick={() => props.addToCart(props.id)}
                    >Add to Cart</button>
                </div>
            </div>
        </div>
    );
}
