import React from 'react';

const Record = () => {
  return (
    <div className='d-flex justify-content-center align-items-center vh-100'>
      <div className='bg-pink fs-4 text-white rounded-5 w-50 p-3'>
        <h2>My Records</h2>
        <h3 className='fw-light'>Audio(s)</h3>
        <form method='POST' action=''>
          <table>
            <thead>
                <th>○</th>
                <th>Name</th>
                <th>Date</th>
                <th>Option</th>
            </thead>    
            <tbody>
                <tr>
                    <td><input type='checkbox'name='check'/></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
            </tbody>
            <div>
              <button className='bg-blue dark-pink rounded m-2 fs-4'>Download selected</button>
              <button className='bg-blue dark-pink rounded m-2 fs-4'>Delete selected</button>
            </div>
          </table>
        </form>
      </div>
    </div>
  );
};

export default Record;