import './App.css';
import Home from './components/screens/Home';


function App() {

  return (
    <div className="App">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
        crossorigin="anonymous"
      />
      <Home/>
    </div>
  );
}

export default App;
var XenElectronicsWebStore = require('xen_electronics_web_store');
window.api = new XenElectronicsWebStore.DefaultApi();