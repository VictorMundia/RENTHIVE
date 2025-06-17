# Django + PostgreSQL Setup for renthive-backend

1. Make sure PostgreSQL is installed and running on your machine.
2. Create a database named `renthive_db` and a user (default: `postgres`).
   - You can use pgAdmin or run:
     ```sql
     CREATE DATABASE renthive_db;
     CREATE USER postgres WITH PASSWORD 'your_password';
     GRANT ALL PRIVILEGES ON DATABASE renthive_db TO postgres;
     ```
   - Replace `your_password` in `settings.py` with your actual password.
3. Install dependencies (already done):
   - `django`, `djangorestframework`, `psycopg2-binary`
4. Run migrations:
   ```pwsh
   cd renthive-backend
   ../.venv/Scripts/python.exe manage.py migrate
   ```
5. Create a superuser:
   ```pwsh
   ../.venv/Scripts/python.exe manage.py createsuperuser
   ```
6. Start the development server:
   ```pwsh
   ../.venv/Scripts/python.exe manage.py runserver
   ```

You are now ready to build your Django backend!
