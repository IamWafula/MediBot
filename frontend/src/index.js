
import React from 'react';
import ReactDOM from 'react-dom/client';
import {StyleReset} from 'atomize';
import App from './App';
import reportWebVitals from './reportWebVitals';

import {Client as Styletron} from 'styletron-engine-atomic';
import {Provider as StyletronProvider} from 'styletron-react';

const root = ReactDOM.createRoot(document.getElementById('root'));
const engine = new Styletron();

root.render(
  <StyletronProvider value={engine}>
    <App /> 
  </StyletronProvider> 
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();  

