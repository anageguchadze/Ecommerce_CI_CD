# Ecommerce_CI_CD

This is a basic eCommerce API built with Django and Django REST Framework. It supports product listings, order creation, and token-based authentication. The project also includes a GitHub Actions CI/CD pipeline for automated testing.

## 🚀 Features

- Product catalog (CRUD)
- Order and Order Items
- Token-based authentication (login to get token)
- User-restricted order access
- PostgreSQL integration
- CI/CD pipeline with GitHub Actions

## 📁 Project Structure

ecommerce_CI_CD/
├── ecommerce_pro/ # Django project
│ ├── settings.py
│ └── urls.py
├── ecommerce_app/ # Main app
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── tests.py
├── requirements.txt
└── .github/
└── workflows/
└── django.yml # GitHub Actions CI/CD config

## 🔧 Setup

1. **Clone the repo**
   git clone https://github.com/anageguchadze/Ecommerce_CI_CD.git
   cd Ecommerce_CI_CD

Create and activate virtualenv
python3 -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Apply migrations
python manage.py migrate

Create superuser (optional)
python manage.py createsuperuser

Run development server
python manage.py runserver

🔐 Authentication
Use token-based authentication.

Obtain token:
POST /api/token/
{
  "username": "yourusername",
  "password": "yourpassword"
}

Use token in requests:
Authorization: Token your_token_here
✅ Run Tests
python manage.py test

⚙️ GitHub Actions CI/CD
This project includes a GitHub Actions workflow that:

Installs dependencies

Runs migrations

Executes tests

Uses PostgreSQL as a service

File: .github/workflows/django.yml

🐘 PostgreSQL Configuration
In settings.py, configure PostgreSQL (or SQLite for local dev).
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce_db',
        'USER': 'postgres',
        'PASSWORD': 'postgresadmin22',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

📫 Contact
For questions, open an issue or reach out at [anageguchadze22@gmail.com].
