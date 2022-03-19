import asyncio
from datetime import datetime

# https://github.com/Fatal1ty/tinkoff-api




async def get_minute_candles():
    # show 1 minute candles for AAPL in 1 year period of time
    async with TinkoffInvestmentsRESTClient(
        token="t.0d0gyqxYtnN4fZSlh7cdORCpIJ6TNxwk5Ksehg-FOxfRoZGdSeW0TNaLMIeMiZNVQTwUpcWjNGa4AEe7bDzcBQ", environment=Environment.SANDBOX
    ) as client:
        bonds = client.market.instruments.get_bonds()
            print(bonds)


asyncio.run(get_minute_candles())
