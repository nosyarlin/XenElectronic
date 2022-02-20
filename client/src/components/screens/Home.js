import React, { useState, useEffect } from 'react';
import Navbar from '../parts/Navbar';
import Card from '../parts/Card';
import { DefaultApi } from 'xen_electronics_web_store';

export default function Home() {
    const [category, setCategory] = useState('home appliances')

    let apiInstance = new DefaultApi();

    useEffect(() => {
        apiInstance.search({category}, (error, data, response) => {
            console.log(error)
            console.log(data)
        })
    })

    return(
        <div>
            <Navbar onClick={setCategory}/>
            <div className="container">
                <Card/>
            </div>
        </div>
    )
}