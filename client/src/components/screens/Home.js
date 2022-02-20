import React, { useState, useEffect } from 'react';
import Navbar from '../parts/Navbar';
import ProductCard from '../parts/ProductCard';
import CartModal from '../parts/CartModal';
import { DefaultApi } from 'xen_electronics_web_store';

export default function Home() {
    const [category, setCategory] = useState('home appliances');
    const [showCart, setShowCart] = useState(false);
    const [products, setProducts] = useState([]);
    const [checkoutProducts, setCheckoutProducts] = useState({});
    const [lastProductAddedToCart, setlastProductAddedToCart] = useState(null);

    // Query for products
    useEffect(() => {
        const apiInstance = new DefaultApi();
        apiInstance.search({category}, (error, data, response) => {
            if (error) {
                console.error(error);
            } else {
                setProducts(data);
            }
        })
    }, [category]);

    // Login
    // Hardcoded for MVP instead of triggered by user behavior
    useEffect(() => {
        const apiInstance = new DefaultApi();
        const requestBody = {
            credentials: {
                username: 'TestUser',
                password: 'password'
            }
        }
        apiInstance.login(
            requestBody,
            (error, data, response) => {
                if (error) {
                    console.error(error);
                }
            });
    });

    function toggleCart() {
        setShowCart(!showCart);
    }

    function addToCart(productId) {
        const product = products.find(p => p.id === productId);
        if (productId in checkoutProducts) {
            setCheckoutProducts({
                ...checkoutProducts,
                [productId]: {
                    ...product,
                    quantity: checkoutProducts[productId].quantity + 1
                }
            });
        } else {
            setCheckoutProducts({
                ...checkoutProducts,
                [productId]: {
                    ...product,
                    quantity: 1
                }
            });
        }
        setlastProductAddedToCart(productId);
    }

    function AddToCartAlert() {
        if (lastProductAddedToCart === null) {
            return null;
        }

        const product = products.find(p => p.id === lastProductAddedToCart);
        return (
            <div className="alert alert-success" role="alert">
                {`Added ${product.name} to cart successfully`}
            </div>
        );
    }

    console.log(checkoutProducts);

    return(
        <div>
            <Navbar onClick={setCategory} toggleCart={toggleCart}/>
            {showCart && <CartModal
                toggleCart={toggleCart}
                checkoutProducts={checkoutProducts}
            />}
            <AddToCartAlert/>
            <div className="container">
                <div className="row">
                    {products.map(
                        product => (
                        <ProductCard
                            key={product.id}
                            id={product.id}
                            name={product.name}
                            price={product.price}
                            addToCart={addToCart}
                        />))}
                </div>
            </div>
        </div>
    )
}