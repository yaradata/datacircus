import React from "react";
import ReactDOM from "react-dom";

import DataProcessing from "./components/dataprocessing/DataProcessing.jsx";

import "./index.css";

import { store } from './app/store'
import { Provider } from 'react-redux'

import UploadDataWithUrl from "./components/dataprocessing/UploadDataWithUrl.jsx"
import UploadData from "./components/dataprocessing/UploadData.jsx";

const App = () => (
  <Provider store={store}>
    <div className="containerFluid bg-info">
      <UploadData/>
      {/* <UploadDataWithUrl/> */}
      {/* <DataProcessing /> */}
    </div>
  </Provider>
);
ReactDOM.render(<App />, document.getElementById("app"));
