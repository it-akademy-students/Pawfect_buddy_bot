import React from 'react';

const Profile = () => {
  return (
    <div class='bg-pink'>
      <h2>Profile</h2>
      <h3>My information</h3>
      <form method='POST' action=''>
        <div>
          <label htmlFor='name'>Name</label>
          <input type='text' name='name' id='name' placeholder='enter user name' />
        </div>
        <div>
          <label htmlFor='email'>Email</label>
          <input type='email' name='email' id='email' placeholder='enter your email' />
        </div>
        <div>
          <label htmlFor='password'>Password</label>
          <input type='password' name='password' id='password' placeholder='enter your password' />
        </div>
        <div>
          <input type='submit' className='bg-blue dark-pink' name='modify' id='modify' value='Modify' />
        </div>
        <a href=''><img src='' alt='' />Back</a>
      </form>
    </div>
  );
};

export default Profile;
