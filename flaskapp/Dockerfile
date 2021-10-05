FROM ubuntu:20.04
RUN apt update && apt upgrade -y && apt install -y python3-flask python3-pip && pip install Flask-WTF
COPY funguj.py /tmp/
COPY templates /tmp/templates
WORKDIR /tmp
ENV FLASK_APP="funguj"
CMD ["flask","run","--host=0.0.0.0"]
