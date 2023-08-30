import React from 'react';

const Checkbox = ({ isChecked, onChange }) => {
  return (
    <input
      type='checkbox'
      checked={isChecked}
      onChange={e => onChange(e.target.checked)}
    />
  );
};

export default Checkbox;