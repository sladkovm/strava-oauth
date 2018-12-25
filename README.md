# strava-oauth
Lightweight python server that implements [Strava Oauth Web Flow](http://developers.strava.com/docs/authentication/)

Install:

```bash
git clone https://github.com/sladkovm/strava-oauth.git
cd strava-oauth
pipenv shell
pipenv install --skip-lock
```

Run:

```python
python api.py
```

Use:

In the web browser go to: *http://127.0.0.1:5042/authorize*

1. You will be redirected to the Strava authorization page
2. After authorization is granted, the browser will display a raw JSON with the authorization tokens
3. Extend and build on it

Example response:

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

Friendly warning: This server is built on [python-responder](https://github.com/kennethreitz/responder), which is an awesome Python API Framework for Humans(TM), but is in active development phase ... that is why I use *--skip-lock* for example. 
