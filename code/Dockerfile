FROM python:3.8-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "manage:app"]
