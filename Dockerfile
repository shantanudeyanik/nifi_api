FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

ENV NAME World

CMD ["/bin/bash" "gunicorn" "-w" "4" "-b" "0.0.0.0:8000" "app:app"]



