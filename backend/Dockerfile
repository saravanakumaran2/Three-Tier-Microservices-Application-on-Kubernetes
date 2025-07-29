FROM python:3.9
WORKDIR /app
COPY server.py /app
RUN apt-get update && apt-get install -y default-mysql-client iputils-ping && rm -rf /var/lib/apt/lists/*
RUN pip install flask mysql-connector-python
CMD ["python", "server.py"]
