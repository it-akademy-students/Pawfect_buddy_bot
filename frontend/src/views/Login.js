import React from 'react';

const LoginView = ({ email, password, onEmailChange, onPasswordChange, onSubmit }) => {
  return (
    <div className='d-flex justify-content-center align-items-center vh-100'>
      <div className='bg-pink fs-4 text-white rounded-5 w-50 p-3'>
        <h2>Connexion</h2>
        <form onSubmit={onSubmit}>
          <div className='d-flex flex-column'>
            <label className='fw-light' htmlFor="email">Email :</label>
            <input type="email" className='fw-light rounded m-2 bg-pale' id="email" value={email} onChange={onEmailChange} required />
          </div>
          <div className='d-flex flex-column'>
            <label className='fw-light' htmlFor="password">Mot de passe :</label>
            <input type="password" className='fw-light rounded m-2 bg-pale' id="password" value={password} onChange={onPasswordChange} required />
          </div>
          <div className='d-flex justify-content-center'>
            <input type="submit" className='bg-blue w-100 dark-pink rounded m-2 fs-4'value='Se connecter' />
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginView;