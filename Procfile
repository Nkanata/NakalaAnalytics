web: gunicorn NakalaAnalytics.wsgi --log-file -
release: python manage.py migrate
release: python ./utils/insertScript.py
