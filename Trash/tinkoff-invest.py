from datetime import datetime, timedelta

import tinkoff.invest
from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.token import TOKEN


def main():
    with Client(TOKEN) as client:
        bonds = client.get_all_boni9pgu9pds()


if __name__ == "__main__":
    main()
