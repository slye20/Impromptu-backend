# Impromptu-backend

Backend of Impromptu, jobs listing project for Orbital 2024.

Built using Django, a high-level Python web framework.

Backend Repository: https://github.com/slidings/impromptuFrontend

Link to Deployed App: https://impromptu-frontend-f9cf.vercel.app/

Creators: Samuel Lim

## Local Setup

Install PostgreSQL, Git and Python 3.11.9 if you haven't already (Python 3.11.9 was used for the development of the application)

Example .env file:

```
# Impromptu/.env
SECRET_KEY=
DB_NAME=impromptu_db
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
```

In pgAdmin4, create databse with name impromptu_db

```
# Clone the repository
git clone https://github.com/slye20/Impromptu-backend
cd Impromptu-backend

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Set up the database
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

And now you can visit the site with the URL http://127.0.0.1:8000/
