import React from 'react';

export default function Navbar(props) {
    return (
        <nav className="navbar navbar-expand-md navbar-light bg-light">
            <ul className="navbar-nav mx-auto">
                <li className="nav-item">
                    <a className="nav-link" href="#" onClick={() => props.onClick('home appliances')}>Home Appliances</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="#" onClick={() => props.onClick('smart watches')}>Smart Watches</a>
                </li>
                <li>
                    <a className="nav-link" href="#" onClick={() => props.onClick('mobile phones')}>Mobile Phones</a>
                </li>
            </ul>
            <ul className="navbar-nav ml-auto">
              <li className="nav-item">
                <button className="btn btn-primary" onClick={props.toggleCart}>Cart</button>
              </li>
            </ul>
        </nav>
    );
}
