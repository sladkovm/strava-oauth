FROM python:3.7

RUN mkdir -p /home/project/strava-oauth
WORKDIR /home/project/strava-oauth
COPY requirements.txt /home/project/strava-oauth
RUN pip install --no-cache-dir -r requirements.txt
COPY . /home/project/strava-oauth
EXPOSE 5042
CMD python api.py