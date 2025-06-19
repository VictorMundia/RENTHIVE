import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Maintenance() {
  const [tickets, setTickets] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/maintenanceticket/')
      .then(res => setTickets(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h1>Maintenance Tickets</h1>
      <ul>
        {tickets.map(ticket => (
          <li key={ticket.id}>{ticket.title}</li>
        ))}
      </ul>
    </div>
  );
}
