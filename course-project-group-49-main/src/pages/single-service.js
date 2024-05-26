import logo from '../FilmFinderLogo.png';
import './single-service.css'
import './services.css';
import React from 'react';
import {useNavigate} from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import $ from 'jquery'

function SingleService() {
  const navigate = useNavigate();
  const navigateHomepage = () => {
    navigate('/homepage');
  };
  const { state } = useLocation();
  const service = state.service;

  function runPyScript(input){
    var jqXHR = $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/search_by_streaming_service?streaming="+service,
        async: false,
        data: { param: input }
    });
    return jqXHR.responseJSON['movies'];
  }
  
    
  // do something with the response
  let response = runPyScript({service});
  console.log(response)

   const navigateMovie= (param) => {
    // 👇️ navigate to /
    navigate('/movie', { state: { movie: param} });
  };

  
  
  return (
    <div>
        <img src={logo} className="logo" alt="logo" onClick={navigateHomepage}/>
      <br></br>
      <p className='head'>{service}</p>

      <div className='container'>
      {runPyScript({service}).map((movie) => {
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

export default SingleService;