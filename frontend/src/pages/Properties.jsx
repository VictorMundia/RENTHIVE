import { useState, useEffect } from 'react';
import axios from 'axios';

export default function Properties() {
  const [properties, setProperties] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/properties/')
      .then(res => setProperties(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h1>Properties Page</h1>
      <ul>
        {properties.map(property => (
          <li key={property.id}>{property.name}</li>
        ))}
      </ul>
    </div>
  );
}
