import logo from '../FilmFinderLogo.png';
import './movie.css'
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

  const movie = state.movie;

  function runPyScript(input){
    var jqXHR = $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/movie_details?name="+movie,
        async: false,
        data: { param: input }
    });
    return jqXHR.responseJSON['movies'];
  }
  
    
  // do something with the response
  let response = runPyScript({movie});

  let services = ""
  for (let i = 0; i < response["streaming"].length; i++) {
    services += response["streaming"][i] + ", "
  }


  return (
    <div >
      {/* <div>
      <header className="header">
        <img src={logo} className="logo" alt="logo" onClick={navigateHomepage}/>
      </header>
      </div> */}
      <img src={logo} className="logo" alt="logo" onClick={navigateHomepage}/>
      <br></br>
      <div className="body">
        <img classname="poster" width="200" height="300" src={response["Poster_Link"]}/>
        <div className='text'>
          <p classname="">Title: {response["Series_Title"]}</p>
          <p>Genre: {response["Genre"]}</p>
          <p>Overview: {response["Overview"]}</p>

          <p>Services available on: {services.substring(0, services.length - 2)}</p>
        </div>
        {/* <p className= 'services'>Available on:</p> 
        <p className= 'services'>{runPyScript({movie})}</p> 
        <p className= 'synopsis-header'>Synopsis</p>   
        <p className= 'synopsis-body'>{runPyScript({movie})}</p>    */}
      </div>
    </div>
    
  );
}

export default SingleGenre;