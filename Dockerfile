FROM python:3.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:5000
