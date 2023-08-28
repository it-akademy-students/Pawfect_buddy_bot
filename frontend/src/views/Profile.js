import React from 'react';

const Profile = () => {
  return (
    <div className='d-flex justify-content-center align-items-center vh-100'>
      <div className='bg-pink fs-4 text-white br-rad p-3'>
        <h2>Profile</h2>
        <h3>My information</h3>
        <form method='POST' action=''>
          <div>
            <label htmlFor='name'>Name</label>
            <input type='text' className='rounded m-2 bg-pale' name='name' id='name' placeholder='enter user name' />
          </div>
          <div>
            <label htmlFor='email'>Email</label>
            <input type='email' className='rounded m-2 bg-pale' name='email' id='email' placeholder='enter your email' />
          </div>
          <div>
            <label htmlFor='password'>Password</label>
            <input type='password' className='rounded m-2 bg-pale' name='password' id='password' placeholder='enter your password' />
          </div>
          <div>
            <input type='submit' className='bg-blue dark-pink rounded m-2 fs-4' name='modify' id='modify' value='Modify' />
          </div>
          <a href='/'><img src='../pic/paw.png' alt='paw' />Back</a>
        </form>
      </div>
    </div>
  );
};

export default Profile;
