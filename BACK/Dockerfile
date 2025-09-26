FROM python:3.12

WORKDIR /BACK

COPY . .

RUN mkdir -p /BACK/logs
RUN touch /BACK/logs/django_error.log /BACK/logs/django_access.log

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary

# Exponer puerto
EXPOSE 8000

# Ejecuta el servidor y comandos necesarios al iniciar
CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py makemigrations && python manage.py migrate && gunicorn IGVA.wsgi:application --bind 0.0.0.0:8000 --error-logfile /BACK/logs/django_error.log"]