import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Leases() {
  const [leases, setLeases] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/leases/')
      .then(res => setLeases(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h1>Leases</h1>
      <ul>
        {leases.map(lease => (
          <li key={lease.id}>{lease.id}</li>
        ))}
      </ul>
    </div>
  );
}
