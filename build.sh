# exit on error
set -o errexit

pip install -r ./requirements.txt

cd noticias
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser --username fisa --email "fisadev@gmail.com" --noinput || true
