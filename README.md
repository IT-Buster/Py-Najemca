# Py-Najemca

Aplikacja do obsługi najemników :))

```bash
$ # Get the code
$ git clone https://github.com/IT-Buster/Py-Najemca.git
$ cd pynajemca
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
$ 
$ python manage.py dumpdata app.model_name --indent 4 > fixtures/file_name.json
$ 
$ python manage.py loaddata user.json
```

