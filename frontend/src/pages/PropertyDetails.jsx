import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

export default function PropertyDetails() {
  const { id } = useParams();
  const [property, setProperty] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8000/api/properties/${id}/`)
      .then(res => setProperty(res.data))
      .catch(err => console.log(err));
  }, [id]);

  if (!property) return <div>Loading...</div>;

  return (
    <div>
      <h1>{property.name}</h1>
      <p>{property.description}</p>
      {/* Add more property details as needed */}
    </div>
  );
}
