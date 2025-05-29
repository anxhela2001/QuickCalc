# Author: Anxhela Halili
# File: Dockerfile
# Purpose: Builds a Docker container for the Flask-based QuickCalc application.
# Dependencies:
#   - Python 3.11 base image
#   - Flask and flask-cors Python packages

FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask flask-cors

EXPOSE 5000

CMD ["python", "app.py"]
