import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Payments() {
  const [payments, setPayments] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/payments/')
      .then(res => setPayments(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h1>Payments</h1>
      <ul>
        {payments.map(payment => (
          <li key={payment.id}>{payment.transaction_id || payment.id}</li>
        ))}
      </ul>
    </div>
  );
}
