import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Tenants() {
  const [tenants, setTenants] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/user/?role=TENANT')
      .then(res => setTenants(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h1>Tenants</h1>
      <ul>
        {tenants.map(tenant => (
          <li key={tenant.id}>{tenant.email}</li>
        ))}
      </ul>
    </div>
  );
}
