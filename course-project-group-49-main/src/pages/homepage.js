import logo from '../FilmFinderLogo.png';
import './homepage.css';
import React from 'react';
import {useNavigate} from 'react-router-dom';



function Homepage() {
  const navigate = useNavigate();
  const navigateServices = () => {
    // 👇️ navigate to /
    navigate('/services');
  };
  const navigateGenres = () => {
    // 👇️ navigate to /
    navigate('/genres');
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
        <p>
          Search by genre or streaming service and get movie recommendations.
        </p>
      <button className="btn" onClick={navigateGenres}>Genre</button>
      <button className="btn" onClick={navigateServices} >Service</button>
    </div>
  );
}

export default Homepage;