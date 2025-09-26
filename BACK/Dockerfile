FROM python:3.12

WORKDIR /back

COPY . .

RUN mkdir -p /back/logs
RUN touch /back/logs/django_error.log /back/logs/django_access.log

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary

# Exponer puerto
EXPOSE 8000

# Ejecuta el servidor y comandos necesarios al iniciar
CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py makemigrations && python manage.py migrate && gunicorn IGVA.wsgi:application --bind 0.0.0.0:8000 --error-logfile /back/logs/django_error.log"]