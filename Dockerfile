FROM python:3.5

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENV DJANGO_SETTINGS_MODULE app.settings
ENV APP_MODE production
ENV DATABASE_URL=sqlite:///test.db

RUN python manage.py collectstatic --noinput

ENTRYPOINT ["gunicorn", "app.wsgi", "-b", "0.0.0.0:9001", "-w", "4", "-t", "30"]

EXPOSE 9001
