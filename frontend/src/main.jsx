import React from 'react';
import ReactDOM from 'react-dom/client'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

import Layout from './components/Layout';

import Home from './pages/Home'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path='/' element={ <Layout /> } >
          <Route index element={ <Home /> } />
        </Route>
      </Routes>
    </Router>
  </React.StrictMode>
)