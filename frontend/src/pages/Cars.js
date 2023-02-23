import React, {useState, useEffect} from 'react';
import CarView from '../components/CarListView';
import axios from 'axios';
export default function Cars() {

    const [carList, setCarList] = useState([{}])
    const [model, setModel] = useState('') 
    const [plate, setPlate] = useState('')
    
      
  
    // Read all cars
    useEffect(() => {
      axios.get('http://localhost:8000/cars')
        .then(res => {
          setCarList(res.data)
        })
    });
  
    // Post a car
    const addCarHandler = () => {
      axios.post('http://localhost:8000/car/', { 'model': model, 'plate': plate })
        .then(res => console.log(res))
  };
  
  
    return (

        <div className="card-body">
        <h5 className="card text-white bg-dark mb-3">Dodaj nowy pojazd</h5>
        <span className="card-text"> 
            <input className="mb-2 form-control modelIn" onChange={event => setModel(event.target.value)} placeholder='Model'/> 
            <input className="mb-2 form-control plateIn" onChange={event => setPlate(event.target.value)}   placeholder='XX XXXXX'/>
            <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}}  onClick={addCarHandler}>Dodaj pojazd</button>
        </span>

        <h5 className="card text-white bg-dark mb-3">Twoje pojazdy</h5>
        <div>
        <CarView carList={carList} />
        </div>
        </div>

);
  }
