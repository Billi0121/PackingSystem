FROM python:3.13-slim

RUN mkdir /app

COPY  requirements.txt /app

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY packing_system/ /app

WORKDIR /app

CMD ["gunicorn", "packing_system.wsgi:application", "--bind", "0:8000"]