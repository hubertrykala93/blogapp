## Installation

Install Python 3.10 and clone the GitHub repository.

```bash
$ git clone https://github.com/hubertrykala93/blogapp.git
$ cd blogapp
```

Create a virtual environment to install dependencies in and activate it:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Install the dependencies:

```bash
(venv)$ pip3 install -r requirements.txt
```

Set the data for your local PostgreSQL database in settings/settings.py.

DATABASE_NAME
DATABASE_USER
DATABASE_PASSWORD
DATABASE_HOST
DATABASE_PORT

Import the data into PostgreSQL.

```bash
(venv)$ python3 manage.py loaddata data/users.json
(venv)$ python3 manage.py loaddata data/posts.json
```

Run the project.

```bash
(venv)$ python3 manage.py runserver
```

And then navigate to ```http://127.0.0.1:8000``` or ```http://localhost:8000```.

<br/>