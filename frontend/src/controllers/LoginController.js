import React, { useState } from 'react';
import UserModel from '../models/UserModel';
import Login from '../views/Login';

const LoginController = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Ici, remplacer consol.log par la verification des informations de connexion au backend.
    console.log('Email:', email);
    console.log('Password:', password);

    // Réinitialisez les champs après la soumission du formulaire.
    setEmail('');
    setPassword('');
  };

  return (
    <Login
      email={email}
      password={password}
      onEmailChange={handleEmailChange}
      onPasswordChange={handlePasswordChange}
      onSubmit={handleSubmit}
    />
  );
};

export default LoginController;