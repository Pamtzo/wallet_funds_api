FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY ./app /app/app
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

