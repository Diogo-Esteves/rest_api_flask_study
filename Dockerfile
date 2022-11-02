FROM python:3.10

EXPOSE 5000

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["/bin/bash", "docker-entrypoint.sh"]
