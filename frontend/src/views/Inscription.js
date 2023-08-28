import React from 'react';

const Inscription = () => {
  return (
    <div className='d-flex justify-content-center align-items-center vh-100'>
      <div className='bg-pink fs-4 text-white br-rad p-3'>
        <h2>Register</h2>
        <h3>Please give me your data</h3>
        <form method='POST' action=''>
          <div>
            <label htmlFor='email'>Email</label>
            <input type='email' className='rounded m-2 bg-pale' name='email' id='email' placeholder='enter your email'/>
          </div>
          <div>
            <label htmlFor='password'>Password</label>
            <input type='password' className='rounded m-2 bg-pale' name='password' id='password' placeholder='enter your password'/>
          </div>
          <div>
            <label htmlFor='confirmPwd'>Confirm Password</label>
            <input type='password' className='rounded m-2 bg-pale' name='confirmPwd' id='confirmPwd' placeholder='confirm your password' />
          </div>
          <div>
            <input type='submit' className='bg-blue dark-pink rounded m-2 fs-4' name='sub' id='sub' value='Submit' />
          </div>
          <a href=''><img src=''/>back</a>
        </form>
      </div>
    </div>
  );
};

export default Inscription;