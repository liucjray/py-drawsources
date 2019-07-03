import urllib.parse as urlparse


def get_qs(url: str, key: str, default):
    parsed = urlparse.urlparse(url)
    return urlparse.parse_qs(parsed.query)[key][0] or default
