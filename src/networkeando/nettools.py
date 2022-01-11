import requests


def get_url(url: str):
    r = requests.get(url)
    if r.status_code == 200:
        return r.status_code, r.text
    else:
        return r.status_code, None
