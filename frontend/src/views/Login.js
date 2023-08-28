import React from 'react';

const LoginView = ({ email, password, onEmailChange, onPasswordChange, onSubmit }) => {
  return (
    <div className='d-flex justify-content-center align-items-center vh-100'>
      <div className='bg-pink fs-4 text-white br-rad p-3'>
        <h2>Connexion</h2>
        <form onSubmit={onSubmit}>
          <div>
            <label htmlFor="email">Email :</label>
            <input type="email" className='rounded m-2 bg-pale' id="email" value={email} onChange={onEmailChange} required />
          </div>
          <div>
            <label htmlFor="password">Mot de passe :</label>
            <input type="password" className='rounded m-2 bg-pale' id="password" value={password} onChange={onPasswordChange} required />
          </div>
          <button type="submit" className='bg-blue dark-pink rounded m-2 fs-4'>Se connecter</button>
        </form>
      </div>
    </div>
  );
};

export default LoginView;