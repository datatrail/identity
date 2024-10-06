FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r ./function/requirements.txt

ENTRYPOINT ["pyhton3", "main.py"]
