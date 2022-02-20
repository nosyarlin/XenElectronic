import React, { useState, useEffect } from 'react';
import Navbar from '../parts/Navbar';
import ProductCard from '../parts/ProductCard';
import CartModal from '../parts/CartModal';
import { DefaultApi } from 'xen_electronics_web_store';
import { useNavigate } from "react-router-dom";

export default function Home(props) {
    const [category, setCategory] = useState('home appliances');
    const [showCart, setShowCart] = useState(false);
    const [products, setProducts] = useState([]);
    const [checkoutProducts, setCheckoutProducts] = useState({});
    const [lastProductAddedToCart, setlastProductAddedToCart] = useState(null);
  
    const navigate = useNavigate(); 


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

    function minusFromCart(productId) {
        const product = products.find(p => p.id === productId);
        if (productId in checkoutProducts && checkoutProducts[productId].quantity > 1) {
            setCheckoutProducts({
                ...checkoutProducts,
                [productId]: {
                    ...product,
                    quantity: checkoutProducts[productId].quantity - 1
                }
            });
        } else {
            let tmpCheckoutProduct = {
                ...checkoutProducts
            }
            delete tmpCheckoutProduct[productId];
            setCheckoutProducts(tmpCheckoutProduct);
        }
    }

    function AddToCartAlert() {
        if (lastProductAddedToCart === null) {
            return null;
        }

        const product = products.find(p => p.id === lastProductAddedToCart);
        if (!product) {
            return null;
        }
        return (
            <div className="alert alert-success" role="alert">
                {`Added ${product.name} to cart successfully`}
            </div>
        );
    }

    function checkout() {
        const apiInstance = new DefaultApi();
        const requestBody = Object.keys(checkoutProducts).map((key) => {
            const checkoutProduct = checkoutProducts[key];
            return {
                productId: checkoutProduct.id,
                quantity: checkoutProduct.quantity
            }
        });
        apiInstance.saveCart({products: requestBody}, (error, data, response) => {
            if (error) {
                console.error(error);
            } else {
                props.setCheckoutId(data['checkoutId']);
            }
        });
        navigate('/checkout');
    }

    return(
        <div>
            <Navbar onClick={setCategory} toggleCart={toggleCart}/>
            {showCart && <CartModal
                toggleCart={toggleCart}
                checkoutProducts={checkoutProducts}
                addToCart={addToCart}
                minusFromCart={minusFromCart}
                checkout={checkout}
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