import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Mode = () => {
  const [showHeaderLinks, setShowHeaderLinks] = useState(false);

  const toggleHeaderLinks = () => {
    setShowHeaderLinks(!showHeaderLinks);
  };

  return (
    <div className='live-video-background'>
      <div className='video-container'>
        <iframe
          src="https://www.youtube.com/embed/jfKfPfyJRdk"
          width="100%"
          height="100%"
          frameBorder="0"
          allowFullScreen
          title="Live Video"
        ></iframe>
        <button onClick={toggleHeaderLinks} className="toggle-header-button">
          {showHeaderLinks ? "Masquer les liens" : "Afficher les liens"}
        </button>
        <div className={`header-container ${showHeaderLinks ? 'show' : ''}`}>
          <header className='pink d-flex justify-content-center align-items-center w-25 fs-4'>
            <nav>
              <ul className='nav flex-column'>
              <li><Link to="/" className="nav-link nav-item" key="home-link">Home</Link></li>
              <li><Link to="/profile" className="nav-link nav-item" key="profile-link">Profile</Link></li>
              <li><Link to="/configuration" className="nav-link nav-item" key="configuration-link">My PBB</Link></li>
              <li><Link to="/record" className="nav-link nav-item" key="record-link">My Records</Link></li>
              </ul>
            </nav>
          </header>
        </div>
      </div>
    </div>
  );
};

export default Mode;
