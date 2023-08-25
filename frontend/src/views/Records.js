import { IonCheckbox } from '@ionic/react';
import React from 'react';

const Record = () => {
  return (
    <div class='bg-pink'>
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
            <button className='bg-blue dark-pink'>Download selected</button>
            <button className='bg-blue dark-pink'>Delete selected</button>
          </table>
        </form>
      </div>
  );
};

export default Record;