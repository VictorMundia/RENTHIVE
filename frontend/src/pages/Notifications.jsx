import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Notifications() {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/notifications/')
      .then(res => setNotifications(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h1>Notifications</h1>
      <ul>
        {notifications.map(note => (
          <li key={note.id}>{note.message}</li>
        ))}
      </ul>
    </div>
  );
}
