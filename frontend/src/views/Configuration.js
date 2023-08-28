import React from 'react';

const Configuration = () => {
  return (
    <div className='d-flex justify-content-center align-items-center vh-100'>
      <div className='bg-pink fs-4 text-white rounded-5 w-50 p-3'>
        <h2>My perfect Buddy Bot</h2>
        <h3 className='fw-light'>Configure my PBB</h3>
        <form method='POST' action=''>
          <div className='d-flex flex-column'>
            <label className='fw-light' htmlFor='code'>Activation code of my PBB</label>
            <input type='text' className='fw-light rounded m-2 bg-pale' name='code' id='code' placeholder='enter your code'/>
          </div>
          <p className='fw-light'> you can find the frame under the frame</p>
          <div className='d-flex justify-content-center'>
            <input type='submit' className='bg-blue w-100 dark-pink rounded m-2 fs-4' name='sub' id='sub' value='Pair my PBB'/>
          </div>
          <a className='a-white' href=''><img src='' alt='paw'/>back</a>
        </form>
      </div>
    </div>
  );
};

export default Configuration;