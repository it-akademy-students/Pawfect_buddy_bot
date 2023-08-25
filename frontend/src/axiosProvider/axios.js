function handleClick() {
    axios.create({
      baseURL: '127.0.0.1:5000',
      headers: {
        Accept: 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true',
        'Content-Type': 'application/json'
      },
      withCredentials: true
    })
  
    axios.get(url:'/test')
      .then(({data}) => {
        console.log('eeeeeee', e)
      });
  }


  import React from 'react';
import axios from 'axios';
import '@ionic/react/css/core.css';
import { setupIonicReact } from '@ionic/react';

setupIonicReact();

const App = () => {
  const handleClick = () => {
    const api = axios.create({
      baseURL: 'http://127.0.0.1:5000',
      headers: {
        Accept: 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true',
        'Content-Type': 'application/json'
      },
      withCredentials: true
    });

    api.get('/test')
      .then(({data}) => {
        console.log('Data:', data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  return (
    <div>
      <h1>Mon application React</h1>
      <button onClick={handleClick}>Effectuer la requête</button>
    </div>
  );
};

export default App;