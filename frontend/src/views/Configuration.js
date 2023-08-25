import React from 'react';

const Configuration = () => {
  return (
    <div class='bg-pink'>
        <h2>My perfect Buddy Bot</h2>
        <h3>Configure my PBB</h3>
        <form method='POST' action=''>
          <div>
            <label for='code'>Activation code of my PBB</label>
            <input type='text' name='code' id='code' placeholder='enter your code'/>
          </div>
          <p> you can find the frame under the frame</p>
          <div>
            <input type='submit' className='bg-blue dark-pink' name='sub' id='sub' value='Pair my PBB'/>
          </div>
          <a href=''><img src=''/>back</a>
        </form>
      </div>
  );
};

export default Configuration;