import { IonCheckbox } from '@ionic/react';
import React from 'react';

const Record = () => {
  return (
    <div className='d-flex justify-content-center align-items-center vh-100'>
      <div className='bg-pink fs-4 text-white br-rad p-3'>
        <h2>My Records</h2>
        <h3>Audio(s)</h3>
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
            <button className='bg-blue dark-pink rounded m-2 fs-4'>Download selected</button>
            <button className='bg-blue dark-pink rounded m-2 fs-4'>Delete selected</button>
          </table>
        </form>
      </div>
    </div>
  );
};

export default Record;