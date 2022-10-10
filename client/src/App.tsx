import React from 'react';
import { Routes } from 'react-router-dom';

import './styles/App.css';

const App = () => {
  return (
    <div>
      <header>
        
      </header>
      <Routes path='/' element={<Main/>}/>
    </div>
  );
}

export default App;
