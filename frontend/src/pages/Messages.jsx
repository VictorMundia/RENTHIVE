import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Messages() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/messages/')
      .then(res => setMessages(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h1>Messages</h1>
      <ul>
        {messages.map(msg => (
          <li key={msg.id}>{msg.content}</li>
        ))}
      </ul>
    </div>
  );
}
