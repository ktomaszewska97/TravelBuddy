FROM python:3.7-alpine

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

WORKDIR /code

COPY ./ ./

RUN apk add --no-cache gcc bash libressl-dev musl-dev libffi-dev \
&& pip install -r requirements.txt

CMD ["flask", "run"]