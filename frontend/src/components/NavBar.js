import React from 'react'
import { Link } from 'react-router-dom'

export default function NavBar() {
  return (
    <div className='nav-bar'>
      <ul>
        <li><Link to={'/'}>Home</Link></li>
        <li><Link to={'/cars'}>Cars</Link></li>
        <li><Link to={'/mileages'}>Mileages</Link></li>
      </ul>
    </div>
  )
}
