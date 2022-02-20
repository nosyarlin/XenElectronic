import React from 'react';

export default function CartModal(props) {

    function CheckoutProductCard({id, name, price, quantity}) {
        return (
            <div className="card d-flex flex-row mb-2">
                <div className="mr-auto">
                    <p>{name}</p>
                    <p>{price}</p>
                </div>
                <p className="ms-auto align-self-center">{`Quantity: ${quantity}`}</p>
                <button className="btn btn-success btm-sm" onClick={() => props.addToCart(id)}>Plus</button>
                <button className="btn btn-danger btn-sm" onClick={() => props.minusFromCart(id)}>Minus</button>
            </div>
        );
    }

    function calculateTotalCost() {
        let cost = 0;
        Object.keys(props.checkoutProducts).map((key) => {
            const checkoutProduct = props.checkoutProducts[key];
            cost += checkoutProduct.price * checkoutProduct.quantity;
            return null;
        });
        return cost;
    }

    return (
        <div className="modal d-block" id="cartModal" tabIndex="-1" role="dialog">
            <div className="modal-dialog" role="document">
                <div className="modal-content">
                    <div className="modal-header">
                        <h5 className="modal-title" id="cartModalLabel">Cart</h5>
                    </div>
                    <div className="modal-body">
                        {Object.keys(props.checkoutProducts).map((key) => {
                            const checkoutProduct = props.checkoutProducts[key];
                            return (
                                <CheckoutProductCard
                                    key={checkoutProduct.id}
                                    id={checkoutProduct.id}
                                    name={checkoutProduct.name}
                                    price={checkoutProduct.price}
                                    quantity={checkoutProduct.quantity}
                                />
                            )})}
                    </div>
                    <p>{`Total: ${calculateTotalCost()}`}</p>
                    <div className="modal-footer">
                        <button type="button" className="btn btn-secondary" onClick={props.toggleCart}>Close</button>
                        <button type="button" className="btn btn-primary" onClick={props.checkout}>Checkout</button>
                    </div>
                </div>
            </div>
        </div>
    );
}
