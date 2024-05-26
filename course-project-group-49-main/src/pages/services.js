import logo from '../FilmFinderLogo.png';
import './services.css';
import React from 'react';
import {useNavigate} from 'react-router-dom';

function Services() {
  const navigate = useNavigate();
  const navigateHomepage = () => {
    // 👇️ navigate to /
    navigate('/homepage');
  };
  const navigateSingleService = (param) => {
    // 👇️ navigate to /
    console.log(param);
    navigate('/singleservice', { state: { service: param} });
  };

  return (
    <div className="Services">
      <header className="service-header">
        <img src={logo} className="service-logo" alt="logo" onClick={navigateHomepage}/>
      </header>
      <button className="service-btn" onClick={event => navigateSingleService("Amazon")}>Amazon Prime</button>
      <button className="service-btn" onClick={event => navigateSingleService('Disney')}>Disney+</button>
      <button className="service-btn" onClick={event => navigateSingleService('Hulu')}>Hulu</button>
      <button className="service-btn" onClick={event => navigateSingleService('Netflix')}>Netflix</button>
      <button className="service-btn" onClick={event => navigateSingleService('Illegal')}>Illegal</button>

    </div>
  );
}

export default Services;