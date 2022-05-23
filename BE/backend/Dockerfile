# https://faun.pub/the-near-perfect-dockerfile-for-django-applications-8bc352a1e871
# Dockerfile for Django Applications

# Section 1- Base Image
FROM python:3.9-slim

# Section 2- Python Interpreter Flags
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Section 3- Compiler and OS libraries
RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && apt-get install ffmpeg libsm6 libxext6 -y \
  && rm -rf /var/lib/apt/lists/*

# Section 4- Project libraries and User Creation
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt 

# Section 5- Code and User Setup
WORKDIR /app
COPY . /app/
ENV WORKERS=2

# Section 6- Docker Run Checks and Configurations
EXPOSE 8000
CMD ["bash", "-c", "python manage.py makemigrations && python manage.py migrate"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "backend.asgi:application"]
