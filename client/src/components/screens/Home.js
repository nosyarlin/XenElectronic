import React, { useState, useEffect } from 'react';
import Navbar from '../parts/Navbar'

export default function Home() {
    const [category, setCategory] = useState('home appliances')

    useEffect(() => {
        console.log(category)
    })

    return(
        <div>
            <Navbar onClick={setCategory}/>
            <div className="container">
            </div>
        </div>
    )
}