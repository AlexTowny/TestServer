FROM alpine:latest

LABEL image_name="back-end-api"

WORKDIR /app 

COPY ./requirements.txt /app/

RUN apk update
RUN apk add --no-cache  gcc musl-dev python3 py3-pip
RUN apk add --no-cache python3-dev musl-dev gcc linux-headers

RUN python3 -m venv .venv

RUN source .venv/bin/activate

RUN pip3 install -r requirements.txt --break-system-packages

COPY . /app/ 

EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "8000"]