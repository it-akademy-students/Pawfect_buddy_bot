import React from 'react';
import './App.scss';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './views/Header';
import InscriptionController from './controllers/InscriptionController';
import LoginController from './controllers/LoginController';
import ForgotPasswordController from './controllers/ForgotPasswordController';
import ProfileController from './controllers/ProfileController';
import HomeController from './controllers/HomeController';
import PairController from './controllers/PairController';
import ModeController from './controllers/ModeController';
import RecordController from './controllers/RecordController';
import ResetController from './controllers/ResetController';


const App = () => {
  const currentPath = window.location.pathname;

  return (
    <Router>
      <div className="d-flex vh-100">
        {currentPath !== '/mode' && <Header />}
        <div className="flex-grow-1">
          <Routes>
            <Route key="home" path="/" element={<HomeController />} />
            <Route key="inscription" path="/inscription" element={<InscriptionController />} />
            <Route key="login" path="/login" element={<LoginController />} />
            <Route key="forgotpassword" path="/forgotpassword" element={<ForgotPasswordController />} />
            <Route key="profile" path="/profile" element={<ProfileController />} />
            
            <Route key="configuration" path="/configuration" element={<PairController />} />
            <Route key="mode" path="/mode" element={<ModeController />} />
            <Route key="record" path="/record" element={<RecordController />} />
            <Route key="reset" path="/reset" element={<ResetController />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;
