release: python manage.py migrate --no-input
web: gunicorn {{ cookiecutter.project_slug }}.wsgi --log-file -