FROM 3.12.0-alpine3.17

WORKDIR /app

# install pip
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

# install dependencies
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
