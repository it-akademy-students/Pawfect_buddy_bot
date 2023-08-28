import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className='pink bg-extra-light-blue d-flex justify-content-center align-items-center w-25 fs-4'>
      <nav>
        <ul className='nav flex-column'>
          <img src={process.env.PUBLIC_URL + '/pic/logo.png'} className='w-75' alt='logo buddyBot'/>
          <li><Link to="/" className="nav-link nav-item">Home</Link></li>
          <li><Link to="/profile" className="nav-link nav-item">Profile</Link></li>
          <li><Link to="/configuration" className="nav-link nav-item">My PBB</Link></li>
          <li><Link to="/record" className="nav-link nav-item">My Records</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;