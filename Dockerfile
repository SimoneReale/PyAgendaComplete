FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Run agenda.py when the container launches
CMD ["python", "agenda.py"]

