// Example: Register a new user
const formData = new FormData();
formData.append('username', 'newuser');
formData.append('email', 'newuser@example.com');
formData.append('password', 'password123');
formData.append('confirm_password', 'password123');
formData.append('role', 'TENANT');
formData.append('phone', '0712345678');
formData.append('national_id', '12345678');
// formData.append('profile_picture', fileInput.files[0]); // Uncomment and use in a real form

fetch('/api/register/', {
  method: 'POST',
  body: formData
})
  .then(res => res.json())
  .then(data => console.log(data));

// Example: Login and get JWT token
fetch('/api/token/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    username: 'newuser',
    password: 'password123'
  })
})
  .then(res => res.json())
  .then(data => {
    localStorage.setItem('access', data.access);
    localStorage.setItem('refresh', data.refresh);
  });

// Example: Use JWT token for authenticated requests
const token = localStorage.getItem('access');
fetch('/api/users/', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
})
  .then(res => res.json())
  .then(data => console.log(data));
