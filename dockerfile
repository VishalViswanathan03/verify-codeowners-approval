FROM python:3.9
WORKDIR /app
COPY src/ /app/src/
RUN pip install -r requirements.txt
CMD ["python", "/app/src/main.py"]
