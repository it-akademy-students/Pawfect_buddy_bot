import React from 'react';

const ForgotPassword = () => {
  return (
    <div class='bg-pink'>
        <h2>Profile</h2>
        <h3>My information</h3>
        <form method='POST' action=''>
          <div>
            <label for='email'>Email</label>
            <input type='email' name='email' id='email' placeholder='enter your email'/>
          </div>
          <div>
            <input type='submit' className='bg-blue dark-pink' name='sub' id='sub' value='Submit'/>
          </div>
          <a href=''><img src=''/>back</a>
        </form>
      </div>
  );
};

export default ForgotPassword;
