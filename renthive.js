// ==========================
// RentHive Backend - Node.js (JavaScript)
// ==========================

// 1. server.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const dotenv = require('dotenv');
const tenantRoutes = require('./routes/tenants');
const complaintRoutes = require('./routes/complaints');
const paymentRoutes = require('./routes/payments');
const authRoutes = require('./routes/auth');

dotenv.config();
const app = express();
app.use(cors());
app.use(express.json());

mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
  .then(() => console.log('MongoDB connected'))
  .catch((err) => console.error(err));

app.use('/api/tenants', tenantRoutes);
app.use('/api/complaints', complaintRoutes);
app.use('/api/payments', paymentRoutes);
app.use('/api/auth', authRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

// 2. models/Tenant.js
const mongoose = require('mongoose');
const TenantSchema = new mongoose.Schema({
  name: String,
  email: { type: String, unique: true },
  password: String,
  unit: String,
  isAdmin: { type: Boolean, default: false }
});
module.exports = mongoose.model('Tenant', TenantSchema);

// 3. models/Complaint.js
const ComplaintSchema = new mongoose.Schema({
  tenantId: mongoose.Schema.Types.ObjectId,
  subject: String,
  description: String,
  status: { type: String, default: 'Pending' },
  createdAt: { type: Date, default: Date.now }
});
module.exports = mongoose.model('Complaint', ComplaintSchema);

// 4. models/Payment.js
const PaymentSchema = new mongoose.Schema({
  tenantId: mongoose.Schema.Types.ObjectId,
  amount: Number,
  method: String,
  status: { type: String, default: 'Confirmed' },
  paidAt: { type: Date, default: Date.now }
});
module.exports = mongoose.model('Payment', PaymentSchema);

// 5. routes/tenants.js
const express = require('express');
const router = express.Router();
const Tenant = require('../models/Tenant');

router.get('/', async (req, res) => {
  const tenants = await Tenant.find();
  res.json(tenants);
});

router.post('/register', async (req, res) => {
  const { name, email, password, unit } = req.body;
  const tenant = new Tenant({ name, email, password, unit });
  await tenant.save();
  res.status(201).json(tenant);
});

module.exports = router;

// 6. routes/complaints.js
const express = require('express');
const router = express.Router();
const Complaint = require('../models/Complaint');

router.post('/', async (req, res) => {
  const { tenantId, subject, description } = req.body;
  const complaint = new Complaint({ tenantId, subject, description });
  await complaint.save();
  res.status(201).json(complaint);
});

router.get('/', async (req, res) => {
  const complaints = await Complaint.find();
  res.json(complaints);
});

module.exports = router;

// 7. routes/payments.js
const express = require('express');
const router = express.Router();
const Payment = require('../models/Payment');

router.post('/', async (req, res) => {
  const { tenantId, amount, method } = req.body;
  const payment = new Payment({ tenantId, amount, method });
  await payment.save();
  res.status(201).json(payment);
});

router.get('/', async (req, res) => {
  const payments = await Payment.find();
  res.json(payments);
});

module.exports = router;

// 8. routes/auth.js (JWT authentication)
const express = require('express');
const jwt = require('jsonwebtoken');
const router = express.Router();
const Tenant = require('../models/Tenant');

router.post('/login', async (req, res) => {
  const { email, password } = req.body;
  const user = await Tenant.findOne({ email });
  if (!user || user.password !== password) {
    return res.status(401).json({ message: 'Invalid credentials' });
  }
  const token = jwt.sign({ id: user._id, isAdmin: user.isAdmin }, process.env.JWT_SECRET);
  res.json({ token });
});

module.exports = router;

// 9. middleware/auth.js (optional)
const jwt = require('jsonwebtoken');

function verifyToken(req, res, next) {
  const token = req.headers.authorization;
  if (!token) return res.status(403).json({ message: 'Token required' });
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    res.status(401).json({ message: 'Invalid token' });
  }
}

module.exports = verifyToken;
