import { useState } from 'react';
import './App.css';
import Home from './components/screens/Home';
import Checkout from './components/screens/Checkout';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";


function App() {
  const [checkoutId, setCheckoutId] = useState(null);
  console.log(checkoutId);

  return (
    <BrowserRouter className="App">
      <Routes>
        <Route path="/home" exact element={<Home setCheckoutId={setCheckoutId}/>}/>
        <Route path="/checkout" element={<Checkout/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
