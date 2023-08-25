import React from 'react';

const Inscription = () => {
  return (
    <div>
      <div>
        <img src='' class=''/>
      </div>
      <div class='bg-pink'>
        <h2>Register</h2>
        <h3>Please give me your data</h3>
        <form method='POST' action=''>
          <div>
            <label htmlFor='email'>Email</label>
            <input type='email' className='bg-transparent' name='email' id='email' placeholder='enter your email'/>
          </div>
          <div>
            <label htmlFor='password'>Password</label>
            <input type='password' className='bg-transparent' name='password' id='password' placeholder='enter your password'/>
          </div>
          <div>
            <label htmlFor='confirmPwd'>Confirm Password</label>
            <input type='password' className='bg-transparent' name='confirmPwd' id='confirmPwd' placeholder='confirm your password' />
          </div>
          <div>
            <input type='submit' className='bg-blue dark-pink' name='sub' id='sub' value='Submit' />
          </div>
          <a href=''><img src=''/>back</a>
        </form>
      </div>
    </div>
  );
};

export default Inscription;