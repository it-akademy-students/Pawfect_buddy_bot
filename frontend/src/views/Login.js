import React from 'react';

const LoginView = ({ email, password, onEmailChange, onPasswordChange, onSubmit }) => {
  return (
    <div class='bg-pink'>
      <h2>Connexion</h2>
      <form onSubmit={onSubmit}>
        <div>
          <label htmlFor="email">Email :</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={onEmailChange}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Mot de passe :</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={onPasswordChange}
            required
          />
        </div>
        <button type="submit" className='bg-blue dark-pink'>Se connecter</button>
      </form>
    </div>
  );
};

export default LoginView;