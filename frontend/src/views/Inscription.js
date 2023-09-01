import React from 'react';

const Inscription = () => {
  return (
    <div className='d-flex justify-content-center align-items-center vh-100'>
      <div className='bg-pink fs-4 text-white rounded-5 w-50 p-3'>
        <h2>Register</h2>
        <h3 className='fw-light'>Please give me your data</h3>
        <form method='POST' action=''>
          <div className='d-flex flex-column'>
            <label className='fw-light' htmlFor='email'>Email</label>
            <input type='email' className='fw-light rounded m-2 bg-pale' name='email' id='email' placeholder='enter your email'/>
          </div>
          <div className='d-flex flex-column'>
            <label className='fw-light' htmlFor='password'>Password</label>
            <input type='password' className='fw-light rounded m-2 bg-pale' name='password' id='password' placeholder='enter your password'/>
          </div>
          <div className='d-flex flex-column'>
            <label className='fw-light' htmlFor='confirmPwd'>Confirm Password</label>
            <input type='password' className='fw-light rounded m-2 bg-pale' name='confirmPwd' id='confirmPwd' placeholder='confirm your password' />
          </div>
          <div className='d-flex justify-content-center'>
            <input type='submit' className='bg-blue w-100 dark-pink rounded m-2 fs-4' name='sub' id='sub' value='Submit' />
          </div>
          <a className='a-white'  href=''><img src=''/>back</a>
        </form>
      </div>
    </div>
  );
};

export default Inscription;