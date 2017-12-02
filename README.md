# django-jp-stations

django-jp-stations is a simple japanese stations apps.

## Quick start

* Add 'django-jp-stations' to requirements.txt

```txt
django-jp-stations
```

* Install the app

```sh
pip install -r requirements.txt
```

* Add "jp-stations" to your INSTALLED_APPS setting like this

```python
INSTALLED_APPS = [
  ...
  'jp_stations',
]
```

* Run `python manage.py migrate` to create the stations models.

## Data

from http://www.ekidata.jp
