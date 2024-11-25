## Installation

Install Python 3.10 and clone the GitHub repository.

```bash
git clone https://github.com/hubertrykala93/blogapp.git
cd blogapp
```

Set up a virtual environment:

```bash
python3.10 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
(venv) pip3 install -r requirements.txt
```

Set up the PostgreSQL database.

```bash
psql -U postgres
CREATE DATABASE blogapp;
```

Configure database settings For example:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogapp',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Apply migrations.

```bash
(venv) python3 manage.py migrate
```

Load initial data.

```bash
(venv) python3 manage.py loaddata data/users.json
(venv) python3 manage.py loaddata data/posts.json
```

 Run the development server.

```bash
(venv)$ python3 manage.py runserver
```

And then navigate to ```http://127.0.0.1:8000``` or ```http://localhost:8000```.
