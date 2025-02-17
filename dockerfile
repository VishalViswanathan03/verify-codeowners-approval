FROM python:3.9

WORKDIR /app

# Copy the entire src directory
COPY src/ . 

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
