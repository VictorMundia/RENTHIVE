// RentHive Frontend (React) & Backend (Node.js/Express)

// Folder Structure:
// - client/    --> React frontend
// - server/    --> Node.js backend
// - shared/    --> Shared interfaces/constants (optional)

// =======================
// 1. FRONTEND - client/
// =======================

// client/src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import Dashboard from './pages/Dashboard';
import PayRent from './pages/PayRent';
import ComplaintForm from './pages/ComplaintForm';
import ApartmentList from './pages/ApartmentList';
import AdminPanel from './pages/AdminPanel';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/pay-rent" element={<PayRent />} />
        <Route path="/complaints" element={<ComplaintForm />} />
        <Route path="/apartments" element={<ApartmentList />} />
        <Route path="/admin" element={<AdminPanel />} />
      </Routes>
    </Router>
  );
}

// (Additional components/pages provided upon request)

// ========================
// 2. BACKEND - server/
// ========================

// server/server.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const dotenv = require('dotenv');
const tenantRoutes = require('./routes/tenants');
const complaintRoutes = require('./routes/complaints');
const paymentRoutes = require('./routes/payments');

dotenv.config();
const app = express();

app.use(cors());
app.use(express.json());

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));

app.use('/api/tenants', tenantRoutes);
app.use('/api/complaints', complaintRoutes);
app.use('/api/payments', paymentRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

// server/models/Tenant.js
const mongoose = require('mongoose');
const TenantSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
  unit: String,
  isAdmin: Boolean,
});
module.exports = mongoose.model('Tenant', TenantSchema);

// (Add similar models for Complaint.js and Payment.js)

// server/routes/tenants.js
const express = require('express');
const router = express.Router();
const Tenant = require('../models/Tenant');

// GET all tenants (Admin only)
router.get('/', async (req, res) => {
  const tenants = await Tenant.find();
  res.json(tenants);
});

// POST register new tenant
router.post('/register', async (req, res) => {
  const { name, email, password, unit } = req.body;
  const newTenant = new Tenant({ name, email, password, unit, isAdmin: false });
  await newTenant.save();
  res.status(201).json(newTenant);
});

module.exports = router;

// Repeat similar pattern for complaints.js and payments.js

// =========================
// ENV File (server/.env)
// =========================
// MONGO_URI=mongodb://localhost:27017/renthive
// JWT_SECRET=your_jwt_secret_key

// =========================
// More pages and backend logic coming up next...
