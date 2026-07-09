import httpx


COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"


COIN_MAP = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana",
    "ADA": "cardano",
}


class MarketService:

    @staticmethod
    async def get_price(symbol: str):

        coin_id = COIN_MAP.get(symbol.upper())

        if not coin_id:
            return None

        params = {
            "ids": coin_id,
            "vs_currencies": "usd",
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    COINGECKO_URL,
                    params=params,
                    timeout=10,
                )

            data = response.json()
            print(data)
            # اگر CoinGecko خطا داد
            if coin_id not in data:
                return None

            return data.get(coin_id, {}).get("usd")

        
        except Exception as e:
            print("MARKET ERROR:", e)
            return None