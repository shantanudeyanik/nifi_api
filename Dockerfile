FROM python:3.11-alpine

LABEL maintainer="shantanudeyanik"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

#ENV NAME World

ENTRYPOINT ["gunicorn"]

#CMD ["app.py"]
CMD ["-w" "4" "-b" "0.0.0.0:8000" "app:app"]



