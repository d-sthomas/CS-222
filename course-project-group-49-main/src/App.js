// import logo from './FilmFinderLogo.png';
import './App.css';
import React from 'react';
import Homepage from './pages/homepage';
import Services from './pages/services';
import Animation from './pages/animation';
// import Movie from './pages/movie';

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Genres from './pages/genres';
import SingleService from './pages/single-service';
import SingleGenre from './pages/single-genre';
import Movie from './pages/movie';

// import { ReactDOM } from 'react';


function App() {
  return (
    // <Homepage></Homepage>
    <Router>
      <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
      </head>
      <Routes>
        <Route path='/' element={<Homepage />} />
        <Route path='/services' element={<Services />} />
        <Route path='/genres' element={<Genres />} />
        <Route path='/homepage' element={<Homepage />} />
        <Route path='/singleservice' element={<SingleService />} />
        <Route path='/singlegenre' element={<SingleGenre />} />
        <Route path='/movie' element={<Movie />} />
      </Routes>
    </Router>
  );
}
 


export default App;
