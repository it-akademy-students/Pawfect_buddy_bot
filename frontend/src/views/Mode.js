import React from 'react';

const Mode = () => {
  return (
    <div className='live-video-background'>
      <iframe
        src="https://www.youtube.com/watch?v=jfKfPfyJRdk"
        width="100%"
        height="100%"
        frameBorder="0"
        allowFullScreen
        title="Live Video"
      ></iframe>
    </div>
  );
};

export default Mode;