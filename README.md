# Django Blog Application

A full-featured blog web application built with Django, ready for deployment on Render.

## Features
- User authentication (signup, login, logout)
- Create, read, update, and delete blog posts
- User-specific blog management
- Responsive UI with Django templates
- SQLite database (default, can be configured for PostgreSQL)

## Project Structure
```
blogapp/         # Main Django app with models, views, templates
blogproject/     # Django project settings and configuration
manage.py        # Django management script
db.sqlite3       # SQLite database (for development)
requirements.txt # Python dependencies
Procfile         # For Render deployment
runtime.txt      # Python version for Render
.env.example     # Environment variable template
```

## Getting Started

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd Blog
```

### 2. Set up environment variables
Copy `.env.example` to `.env` and fill in the required values:
```bash
cp .env.example .env
```

### 3. Install dependencies
It is recommended to use a virtual environment:
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (optional, for admin access)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Deployment on Render
1. Push your code to a GitHub repository.
2. Create a new Web Service on [Render](https://render.com/).
3. Connect your repository and set the build and start commands:
   - **Build Command:** `pip install -r requirements.txt && python manage.py migrate`
   - **Start Command:** `gunicorn blogproject.wsgi:application`
4. Add environment variables in the Render dashboard (see `.env.example`).
5. Deploy!

## License
This project is licensed under the MIT License.

---

**Happy blogging!**
