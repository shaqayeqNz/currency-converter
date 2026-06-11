import requests
from cachetools import cached, TTLCache
from src.config import CACHE_TTL, API_URL

cache = TTLCache(maxsize=100, ttl=CACHE_TTL)


@cached(cache)
def get_exchange_rate(base_currency, target_currency):
    try:
        url = f"{API_URL}{base_currency}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        return data["rates"].get(target_currency)

    except requests.RequestException:
        return None