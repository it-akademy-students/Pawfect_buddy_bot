import React from 'react';

const Configuration = () => {
  return (
    <div className='d-flex justify-content-center align-items-center vh-100'>
      <div className='bg-pink fs-4 text-white br-rad p-3'>
        <h2>My perfect Buddy Bot</h2>
        <h3>Configure my PBB</h3>
        <form method='POST' action=''>
          <div>
            <label htmlFor='code'>Activation code of my PBB</label>
            <input type='text' className='rounded m-2 bg-pale' name='code' id='code' placeholder='enter your code'/>
          </div>
          <p> you can find the frame under the frame</p>
          <div>
            <input type='submit' className='bg-blue dark-pink rounded m-2 fs-4' name='sub' id='sub' value='Pair my PBB'/>
          </div>
          <a href=''><img src=''/>back</a>
        </form>
      </div>
    </div>
  );
};

export default Configuration;