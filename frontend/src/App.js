import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import Cars from './pages/Cars';
import { Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import NavBar from './components/NavBar';
import Mileages from './pages/Mileages';
import Home from './pages/Home';

function App() {
  return (
    <div className="App list-group-item  justify-content-center align-items-center mx-auto" >
      <Header />
      <NavBar />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/cars' element={<Cars />} />
        <Route path='/mileages' element={<Mileages />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
