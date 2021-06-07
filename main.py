from ibapi.client import EClient
from ibapi.common import BarData
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

import threading
import time


class IBapi(EWrapper, EClient):
    def __init__(self, host, port, client_id):
        EClient.__init__(self, self)
        self.connect(host, port, client_id)

    def historicalData(self, reqId: int, bar: BarData):
        print(bar.close)


def run(app: IBapi):
    app.run()


def create_contract(symbol):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = 'STK'
    contract.exchange = 'SMART'
    contract.currency = 'USD'
    return contract


if __name__ == '__main__':

    app = IBapi('127.0.0.1', 7497, 123)


    # Start the socket in a thread
    api_thread = threading.Thread(target=run, args=[app])
    api_thread.start()

    time.sleep(1)  # Sleep interval to allow time for connection to server

    # Create contract object
    su_contract = create_contract('SU')

    # Request Market Data
    app.reqHistoricalData(11, su_contract, "", "1 M", "5 mins", "MIDPOINT", True, 1, True, [])

    time.sleep(5)  # Sleep interval to allow time for incoming price data
    app.disconnect()
