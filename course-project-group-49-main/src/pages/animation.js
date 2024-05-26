import logo from '../FilmFinderLogo.png';
import './animation.css';
import React from 'react';
import {useNavigate} from 'react-router-dom';


function Animation() {
    const navigate = useNavigate();
    const navigateHomepage = () => {
      // 👇️ navigate to /
      navigate('/homepage');
    };
    const navigateMovie = () => {
        // 👇️ navigate to /
        navigate('/movie');
      };
  
    return (
      <div className="Animation">
        <header className="animation-header">
          <img src={logo} className="animation-logo" alt="logo" onClick={navigateHomepage} />
        </header>
        <div class="left-padding"/>
        <button className="btn" onClick={navigateMovie}>Despicable Me</button>
        <div class="divider"/>
        <button className="btn" onClick={navigateMovie}>Despicable Me 2</button>
        <div class="left-padding"/>
        <button className="btn" onClick={navigateMovie}>Despicable Me 3</button>
        <div class="divider"/>
        <button className="btn" onClick={navigateMovie}>Minions</button>
        <div class="left-padding"/>
        <button className="btn" onClick={navigateMovie}>Minons: Rise of Gru</button>
        
      </div>
    );
  }
  
  export default Animation;