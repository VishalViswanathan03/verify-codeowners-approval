FROM python:3.9

WORKDIR /app

COPY src/main.py .
COPY src/requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
