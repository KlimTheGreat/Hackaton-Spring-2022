import asyncio
from datetime import datetime

# https://github.com/Fatal1ty/tinkoff-api

<<<<<<< HEAD



async def get_minute_candles():
    # show 1 minute candles for AAPL in 1 year period of time
    async with TinkoffInvestmentsRESTClient(
        token="t.0d0gyqxYtnN4fZSlh7cdORCpIJ6TNxwk5Ksehg-FOxfRoZGdSeW0TNaLMIeMiZNVQTwUpcWjNGa4AEe7bDzcBQ", environment=Environment.SANDBOX
    ) as client:
        bonds = client.market.instruments.get_bonds()
            print(bonds)
=======
from tinkoff.investments import (
    CandleResolution,
    Environment,
    TinkoffInvestmentsRESTClient,
)

from tinkoff.investments.client.exceptions import TinkoffInvestmentsError
from tinkoff.investments.utils.historical_data import HistoricalData


async def get_bonds():
    try:
        async with TinkoffInvestmentsRESTClient(
                token="t.0d0gyqxYtnN4fZSlh7cdORCpIJ6TNxwk5Ksehg-FOxfRoZGdSeW0TNaLMIeMiZNVQTwUpcWjNGa4AEe7bDzcBQ",
                environment=Environment.SANDBOX
        ) as client:
            bonds = await client.market.instruments.get_bonds()
            historical_data = HistoricalData(client)
            for bond in bonds:
                candles = historical_data.iter_candles(
                        figi=bond.figi,
                        dt_from=datetime(2022, 1, 12),
                        dt_to=datetime(2022, 1, 13),
                        interval=CandleResolution.DAY,
                )
                print(bond.isin, ":", candles[0], "руб")
    except TinkoffInvestmentsError as e:
        print(e)
>>>>>>> origin/main


asyncio.get_event_loop().run_until_complete(get_bonds())
