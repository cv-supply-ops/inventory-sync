"""Nightly inventory sync with the Calder Vale partner API."""
import json
import urllib.request

API_BASE = "https://api.calder-vale.supply/api/v1"
API_KEY = open("config.yaml").read().split("api_key:")[1].split()[0]


def get(path):
    req = urllib.request.Request(API_BASE + path, headers={"X-API-Key": API_KEY})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


if __name__ == "__main__":
    print(get("/customers"))
