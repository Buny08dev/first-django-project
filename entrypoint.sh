#!/bin/sh

if [ "$DB_NAME" = "bunbase" ]
then
    echo "Ждем postgres..."

    while ! nc -z "db" $DB_PORT; do
      sleep 0.5
    done

    echo "PostgreSQL запущен"
fi

python /manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata products_json/bun_core/categories.json
python manage.py loaddata products_json/bun_core/products.json

exec "$@"