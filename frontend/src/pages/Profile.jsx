import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Profile() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/api/user/me/')
      .then(res => setUser(res.data))
      .catch(err => console.log(err));
  }, []);

  if (!user) return <div>Loading...</div>;

  return (
    <div>
      <h1>Profile</h1>
      <p>Email: {user.email}</p>
      {/* Add more user details as needed */}
    </div>
  );
}
