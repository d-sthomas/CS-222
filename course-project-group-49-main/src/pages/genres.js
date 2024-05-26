import logo from '../FilmFinderLogo.png';
import './genres.css';
import React from 'react';
import {useNavigate} from 'react-router-dom';


function Genres() {
  const navigate = useNavigate();
  const navigateHomepage = () => {
    // 👇️ navigate to /
    navigate('/homepage');
  };
  const navigateAnimation = () => {
    // 👇️ navigate to /
    navigate('/animation');
  };

  const navigateSingleGenre = (param) => {
    // 👇️ navigate to /
    navigate('/singlegenre', { state: { genre: param} });
  };

  return (
    <div className="Genres">
      <header className="genre-header">
        <img src={logo} className="genre-logo" alt="logo" onClick={navigateHomepage} />
      </header>
      <button className="genre-btn" onClick={event => navigateSingleGenre("Crime")}>Crime</button>
      <button className="genre-btn" onClick={event => navigateSingleGenre("Drama")}>Drama</button>
      <button className="genre-btn" onClick={event => navigateSingleGenre("Action")}>Action</button>
      <button className="genre-btn" onClick={event => navigateSingleGenre("Adventure")}>Adventure</button>
      {/* <button className="genre-btn" onClick={event => navigateSingleGenre("International")}>International</button> */}
      {/* <button className="genre-btn" onClick={event => navigateSingleGenre("Suspense")}>Suspense</button> */}
      {/* <button className="genre-btn" onClick={event => navigateSingleGenre("Kids")}>Kids</button> */}
      <button className="genre-btn" onClick={event => navigateSingleGenre("Fantasy")}>Fantasy</button>
    </div>
  );
}

export default Genres;