import React from 'react';

const Profile = () => {
  return (
    <div className='d-flex justify-content-center align-items-center vh-100'>
      <div className='bg-pink fs-4 text-white rounded-5 w-50 p-3'>
        <h2>Profile</h2>
        <h3 className='fw-light'>My Informations</h3>
        <form method='POST' action=''>
          <div className='d-flex flex-column'>
            <label className='fw-light' htmlFor='name'>Name</label>
            <input type='text' className='fw-light rounded m-2 bg-pale' name='name' id='name' placeholder='Enter user name' />
          </div>
          <div className='d-flex flex-column'>
            <label className='fw-light' htmlFor='email'>Email</label>
            <input type='email' className='fw-light rounded m-2 bg-pale' name='email' id='email' placeholder='Enter your email' />
          </div>
          <div className='d-flex flex-column'>
            <label className='fw-light' htmlFor='password'>Password</label>
            <input type='password' className='fw-light rounded m-2 bg-pale' name='password' id='password' placeholder='Enter your password' />
          </div>
          <div className='d-flex justify-content-center'>
            <input type='submit' className='bg-blue w-100 dark-pink rounded m-2 fs-4' name='modify' id='modify' value='Modify' />
          </div>
          <a className='a-white' href='/'><img src='../pic/paw.png' alt='paw' />Back</a>
        </form>
      </div>
    </div>
  );
};

export default Profile;
