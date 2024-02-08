import React, { useState, useEffect } from 'react';
import HomePage from './components/homePage';
import Ingredients from './components/ingredients'
import ButtonAppBar from './components/appBar'

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import axios from "axios"

function App() {
  const [ingredients, setIngredients] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (loading) {
      fetchData();
    }
  }, [loading])

  const fetchData = () => {
    axios.get(`http://localhost:5000/api/ingredients`)
    .then(response => {
      console.log('getIngredients response', response)
      setIngredients(response.data)
      setLoading(false)
    })
  }

  console.log("I", ingredients)

  return (
    <div>
      <Router>
        <ButtonAppBar />
        <Routes>
          <Route path="/" element={<HomePage />}/>
          <Route path="/ingredients" element={ <Ingredients ingredients={ingredients}/> }/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;