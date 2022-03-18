

import asyncio
from datetime import datetime
import  tinkoff

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
        bonds = client.market.instruments.get_bonds()


asyncio.run(get_minute_candles())

