from app.config import settings

from app.backend.src.http_client import CMPHTTPClient


cmp_client = CMPHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMP_TOKEN
)
