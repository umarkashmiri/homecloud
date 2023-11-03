FROM python:3.12

COPY /requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY / /code/app

WORKDIR /code/app

CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]
