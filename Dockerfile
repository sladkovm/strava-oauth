FROM python:3.7-alpine
RUN mkdir -p /app
RUN apk add --no-cache build-base
COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt \
    && apk del build-base

COPY api.py /app

EXPOSE 5042

WORKDIR /app
CMD python api.py