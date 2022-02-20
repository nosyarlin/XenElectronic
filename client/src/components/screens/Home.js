import React, { useState, useEffect } from 'react';
import Navbar from '../parts/Navbar';
import ProductCard from '../parts/ProductCard';
import CartModal from '../parts/CartModal';
import { DefaultApi } from 'xen_electronics_web_store';

export default function Home() {
    const [category, setCategory] = useState('home appliances');
    const [products, setProducts] = useState([]);

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
                    console.log(response);
                }
            });
    });

    return(
        <div>
            <Navbar onClick={setCategory}/>
            <CartModal/>
            <div className="container">
                <div className="row">
                    {products.map(
                        product => (
                        <ProductCard
                            key={product.id}
                            id={product.id}
                            name={product.name}
                            price={product.price}
                        />))}
                </div>
            </div>
        </div>
    )
}