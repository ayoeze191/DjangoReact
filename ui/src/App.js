import React, { useEffect } from 'react'
import Header from './components/Header'
import { HashRouter as Router, Route, Routes } from 'react-router-dom';
import axios from 'axios';
const App = () => {
  useEffect(() => {
    axios.get('/Test')
    .then((res) => console.log(res.data))
  })


  return (
    <div>
      <Router>
      Hello From React!
      <Routes>
      <Route element= {<Header />} path = "/header" />
      </Routes>
      </Router>
    </div>
  )
}

export default App