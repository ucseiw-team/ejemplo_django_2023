# exit on error
set -o errexit

cd noticias
gunicorn noticias.wsgi:application
