import DeepChatBrowser from '../../../components/table/deepChatBrowser';
import './captureFiles.css';
import React from 'react';

function RightPanel() {
  return (
    <div id="column-types-right">
      <div className="column-types-text">
        As well as uploading files into the chat, you can use it to create them! Click the camera button to capture photos
        or use the microphone button to record audio.
      </div>
    </div>
  );
}

function LeftPanel() {
  return (
    <div id="column-types-left">
      <DeepChatBrowser
        existingService={{demo: true}}
        introMessage={`Click the camera or the microphone button.`}
        initialMessages={[
          {file: {src: '/img/cat.jpg', type: 'image'}, role: 'user'},
          {file: {src: '/audio/jeff.mp3', type: 'audio'}, role: 'ai'},
        ]}
        containerStyle={{
          borderRadius: '10px',
          boxShadow: '0 .5rem 1rem 0 rgba(44, 51, 73, .1)',
          borderColor: '#ededed',
          marginLeft: '30px',
          marginRight: '30px',
        }}
        camera={{button: {styles: {container: {default: {marginRight: '2px'}}}}}}
        microphone={{button: {styles: {container: {default: {marginLeft: '4px'}}}}}}
        textInput={{
          styles: {
            container: {
              width: '75%',
            },
          },
        }}
      ></DeepChatBrowser>
    </div>
  );
}

export default function CaptureFiles() {
  return (
    <div id="customization">
      <div className="feature-sub-header" style={{marginTop: '150px'}}>
        Camera and Microphone
      </div>
      <div id="column-types">
        <LeftPanel></LeftPanel>
        <RightPanel></RightPanel>
      </div>
    </div>
  );
}