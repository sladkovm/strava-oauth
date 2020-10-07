# strava-oauth
Lightweight python server that implements [Strava Oauth Web Flow](http://developers.strava.com/docs/authentication/)


This repo comes with pre-configured *Dockerfile* and *docker-compose.yml*, which allows direct deployment by simply running:

```bash
make build
```

## Must

Before using set environmental variables that represent your [application](https://www.strava.com/settings/api):

```bash
export STRAVA_CLIENT_ID=<the-actual-id>
export STRAVA_CLIENT_SECRET=<the-actual-secret>
```

## Quick start

```bash
git clone https://github.com/sladkovm/strava-oauth.git
cd strava-oauth
pipenv shell
pipenv install --pre
```

Run the server:

```python
python api.py
```

In the web browser go to: *http://127.0.0.1:5042/authorize*

1. You will be redirected to the Strava authorization page
2. After authorization is granted, the browser will display a raw JSON with the authorization tokens
3. Take it from here and build on it

```
Example Response
{
  "token_type": "Bearer",
  "access_token": "987654321234567898765432123456789",
  "athlete": {
    #{summary athlete representation}
  },
  "refresh_token": "1234567898765432112345678987654321",
  "expires_at": 1531378346,
  "state": "https://github.com/sladkovm/strava-oauth"
}
```

## Run as a dockerized application

First you need to build docker image from source code. This might take a while so be patient.

```bash
docker build -t strava-oauth .
```

After image is succesfully built, you can run it in docker container. Make sure you provide STRAVA_CLIENT_ID and STRAVA_CLIENT_SECRET to docker container.

```bash
docker container run --rm  -p 5042:5042 --e STRAVA_CLIENT_ID=<the-actual-id> -e STRAVA_CLIENT_SECRET=<the-actual-secret> strava-oauth:latest
```

Before you start, the container also make sure you provide APP_URL if you are not working on http://localhost:5047

```bash
docker container run --rm  -p 5042:5042 -e STRAVA_CLIENT_ID=<the-actual-id> -e STRAVA_CLIENT_SECRET=<the-actual-secret> -e APP_URL="http://dev.myapp.com" strava-oauth:latest
```
In this case the callbacks will be redirected to `http://dev.myapp.com:5042/authorization_successful`

Some gotchas:

1. If you run docker directly from the terminal (e.g. not in the docker-machine), the docker containers will be spawned at the *localhost*. In this case you don't need to specify the *APP_URL*. The server will be run as in the *Quick start* case - at *http://127.0.0.1:5042/authorize*

2. If you run docker on the *docker-machine*, with a given IP, you will need to figure out how to redirect to this IP. The easiest way is to set `export APP_URL=dev.myapp.com`. Then add to the */etc/hosts* the following line: `<docker-machine IP>  dev.myapp.com`. This will send all Strava redirects to the docker-machine IP

3. Majority of browsers are caching redirect requests which means that your http://localhost:5042/authorize might get cached. If you changed your STRAVA_CLIENT_ID make sure that your browser is not returning you cached redirect.



## Friendly warning
This server is built on [python-responder](https://github.com/kennethreitz/responder), which is an awesome Python API Framework for Humans(TM), but is in active development phase ... that is why I use *--pre* and *--skip-lock* for example.
