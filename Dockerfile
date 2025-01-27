FROM python:3.12.4

WORKDIR /app

# install dependecy

COPY requirement.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install gunicorn

# collect static files
RUN python manage.oy collectstatic --no-input --no-input

# run django server with gunicorn

CMD [ "gunicorn", "--bind", "0.0.0.0.8000","hello.wsgi:application" ]