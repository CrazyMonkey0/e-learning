FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERD=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y \
    libmemcached11 \
    libmemcachedutil2 \
    libmemcached-dev \
    libz-dev
RUN pip install -r  requirements.txt
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY . /code/