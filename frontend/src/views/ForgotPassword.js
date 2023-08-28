import React from 'react';

const ForgotPassword = () => {
  return (
    <div className='d-flex justify-content-center align-items-center vh-100'>
      <div className='bg-pink fs-4 text-white br-rad p-3'>
        <h2>Profile</h2>
        <h3>My information</h3>
        <form method='POST' action=''>
          <div>
            <label for='email'>Email</label>
            <input type='email' className='rounded m-2 bg-pale' name='email' id='email' placeholder='enter your email'/>
          </div>
          <div>
            <input type='submit' className='bg-blue dark-pink rounded m-2 fs-4' name='sub' id='sub' value='Submit'/>
          </div>
          <a href=''><img src=''/>back</a>
        </form>
      </div>
    </div>
  );
};

export default ForgotPassword;
