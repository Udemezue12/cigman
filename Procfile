release: python manage.py makemigrations --no-input && python manage.py migrate --no-input


web: waitress-serve --port=$PORT portfolio_project.wsgi:application


worker: celery -A portfolio_project worker -l info
