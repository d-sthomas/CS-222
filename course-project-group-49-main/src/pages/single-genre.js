import logo from '../FilmFinderLogo.png';
import './single-genre.css'
import React from 'react';
import {useNavigate} from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import $ from 'jquery'


function SingleGenre() {
  const navigate = useNavigate();
  const navigateHomepage = () => {
    navigate('/homepage');
  };

  const { state } = useLocation();
  const genre = state.genre;

  function runPyScript(input){
    var jqXHR = $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/search_by_genre?genre="+genre,
        async: false,
        data: { param: input }
    });
    return jqXHR.responseJSON['movies'];
  }

  const navigateMovie= (param) => {
    // 👇️ navigate to /
    navigate('/movie', { state: { movie: param} });
  };
  

  let response = runPyScript({genre});
  console.log(response);

  return (
    <div>
       <img src={logo} className="logo" alt="logo" onClick={navigateHomepage}/>
      <br></br>
      <p className='head'>{genre}</p>
      
      <div className='container'>
      {runPyScript({genre}).map((movie) => {
    return (
        <div
        key={movie["Series_Title"]}
          className='containerItem'
        >
          {/* height ="200" width="180"  */}
          <img src={movie["Poster_Link"]} onClick={event => navigateMovie(movie["Series_Title"])}/>
          <p className='movieTitle'>{movie["Series_Title"]}</p>
        </div>
        
    );
  })}

      </div>
      
    </div>
    
  );
}

export default SingleGenre;