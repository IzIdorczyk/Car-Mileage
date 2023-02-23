import axios from 'axios'
import React from 'react'

function CarItem(props) {
    const deleteCarHandler = (plate) => {
    axios.delete(`http://localhost:8000/car/${plate}`)
        .then(res => console.log(res.data)) }
  
    return (
        <div>
            <p>
                <span style={{ fontWeight: 'bold, underline' }}>{props.car.model}: </span> {props.car.plate} 
                <button onClick={() => deleteCarHandler(props.car.plate)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px',}}>Usuń pojazd</button>
                <hr></hr>
            </p>
        </div>
    )
}

export default CarItem;
