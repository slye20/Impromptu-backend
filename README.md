# Impromptu-backend

Backend of Impromptu, an online shop for Orbital 2024. Built using Django, a high-level Python web framework.

## Download Instructions

Install Git and Python 3.11.9 if you haven't already (Python 3.11.9 was used for the development of the application)

```
# Clone the repository
git clone https://github.com/slye20/Impromptu-backend
cd Impromptu

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
