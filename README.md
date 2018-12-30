# strava-oauth
Lightweight python server that implements [Strava Oauth Web Flow](http://developers.strava.com/docs/authentication/)


Example app is running at [Get a Strava Token](http://velometria.com/strava-oauth/authorize)

**Warning:** The example app does not store the issued token or any other information receieved from the Strava API. The token however is issued on behalf of the [velometria.com](http://velometria.com) so please use responsibly. The token will expire in 6 hours.

Try the freshly fetched token together with a Python library for Strava API [stravaio](https://github.com/sladkovm/stravaio)

## Install:

```bash
git clone https://github.com/sladkovm/strava-oauth.git
cd strava-oauth
pipenv shell
pipenv install --pre
```

If the installation fails on dependencies try:

```bash
pipenv install --skip-lock
```

## Run:

Before run set environmental variables that represent your [application](https://www.strava.com/settings/api):

```bash
export STRAVA_CLIENT_ID=<the-actual-id>
export STRAVA_CLIENT_SECRET=<the-actual-secret>
```

```python
python api.py
```

## Use:

In the web browser go to: *http://127.0.0.1:5042/authorize*

1. You will be redirected to the Strava authorization page
2. After authorization is granted, the browser will display a raw JSON with the authorization tokens
3. Extend and build on it

## Example response:

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

## Friendly warning
This server is built on [python-responder](https://github.com/kennethreitz/responder), which is an awesome Python API Framework for Humans(TM), but is in active development phase ... that is why I use *--pre* and *--skip-lock* for example.
