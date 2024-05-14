from fastapi import APIRouter

from app.backend.src import cmp_client

from async_lru import alru_cache

router = APIRouter(prefix="/cryptocurrencies", tags=["Currencies"])


@router.get("")
async def get_cryptocurrencies():

    return await cmp_client.get_listings()


@router.get("/{currency_id}")
async def get_cryptocurrency_by_id(currency_id: int):

    return await cmp_client.get_currency(currency_id)
