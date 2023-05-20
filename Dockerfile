# Use an official Python runtime as a parent image
FROM python:3.9

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Copy the current directory contents into the container at /app
WORKDIR /app
COPY ./core /app

# Start the Django app
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
