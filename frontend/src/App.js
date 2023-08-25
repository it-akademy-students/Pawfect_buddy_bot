import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
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
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomeController />} />
        <Route path="/inscription" element={<InscriptionController />} />
        <Route path="/login" element={<LoginController />} />
        <Route path="/forgotpassword" element={<ForgotPasswordController />} />
        <Route path="/profile" element={<ProfileController />} />
        
        <Route path="/configuration" element={<PairController />} />
        <Route path="/mode" element={<ModeController />} />
        <Route path="/record" element={<RecordController />} />
        <Route path="/reset" element={<ResetController />} />
      </Routes>
    </Router>
  );
};

export default App;
