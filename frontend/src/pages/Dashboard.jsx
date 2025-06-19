import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Dashboard() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/api/user/me/')
      .then(res => setUser(res.data))
      .catch(err => console.log(err));
  }, []);

  if (!user) return <div>Loading...</div>;

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Welcome, {user.email}</p>
    </div>
  );
}
