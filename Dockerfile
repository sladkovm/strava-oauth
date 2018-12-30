FROM python:3.6.7

RUN mkdir -p /home/project/strava-oauth
WORKDIR /home/project/strava-oauth
COPY Pipfile /home/project/strava-oauth
RUN pip install pipenv
RUN pipenv install --skip-lock
# RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/strava-oauth

EXPOSE 5042

CMD pipenv run python api.py