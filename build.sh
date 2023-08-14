# exit on error
set -o errexit

pip install -r ./requirements.txt

find . | grep manage.py
cd $(dirname $(find . | grep manage.py))
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser --username fisa --email "fisadev@gmail.com" --noinput || true
