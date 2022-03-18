import asyncio
from datetime import datetime

# https://github.com/Fatal1ty/tinkoff-api

from tinkoff.investments import (
    CandleResolution,
    Environment,
    TinkoffInvestmentsRESTClient,
)
from tinkoff.investments.utils.historical_data import HistoricalData


async def get_minute_candles():
    # show 1 minute candles for AAPL in 1 year period of time
    async with TinkoffInvestmentsRESTClient(
        token="t.0d0gyqxYtnN4fZSlh7cdORCpIJ6TNxwk5Ksehg-FOxfRoZGdSeW0TNaLMIeMiZNVQTwUpcWjNGa4AEe7bDzcBQ", environment=Environment.SANDBOX
    ) as client:
        client.market.instruments.get_bonds()
        historical_data = HistoricalData(client)
        async for candle in historical_data.iter_candles(
            figi="BBG000B9XRY4",
            dt_from=datetime(2022, 1, 1),
            dt_to=datetime(2022, 2, 1),
            interval=CandleResolution.MIN_1,
        ):
            print(candle)


asyncio.run(get_minute_candles())
