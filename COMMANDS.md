# django-dev

## Setup
```
python -m pip install --upgrade pip
pip install virtualenv
python -m venv ./venv
./venv/Scripts/activate.bat
pip install -r requirements.txt
python manage.py migrate
```

## Execute
```
./venv/Scripts/activate.bat
python manage.py runserver
```