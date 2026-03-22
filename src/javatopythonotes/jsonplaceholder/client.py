"""HTTP client for JSONPlaceholder — https://jsonplaceholder.typicode.com (free, no API key)."""

import json
from typing import Any, Dict
from urllib.request import urlopen

BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_post(post_id: int) -> Dict[str, Any]:
    """GET /posts/{post_id} and return the JSON object as a dict."""
    if post_id < 1:
        raise ValueError("post_id must be >= 1")
    url = f"{BASE_URL}/posts/{post_id}"
    with urlopen(url, timeout=15) as response:
        raw = response.read().decode("utf-8")
    return json.loads(raw)
