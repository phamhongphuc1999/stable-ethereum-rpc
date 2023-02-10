import time

from stable_ethereum_rpc.stable_web3 import StableWeb3
from stable_ethereum_rpc.web3_list import Web3Entity

raw_web3_list = [
    {"url": "https://bsc-dataseed.binance.org", "type": "http"},
    {"url": "https://bsc-dataseed1.binance.org", "type": "http"},
    {"url": "https://bsc-dataseed1.defibit.io", "type": "http"},
    {"url": "https://bsc-dataseed2.defibit.io", "type": "http"},
    {"url": "https://bsc-dataseed1.ninicoin.io", "type": "http"},
    {"url": "https://bsc-dataseed2.ninicoin.io", "type": "http"},
]


def web3_callback_func(web3: Web3Entity, params: object):
    print(f"web3: {web3.rpc}, result: {params}")


if __name__ == "__main__":
    stable_web3 = StableWeb3(raw_web3_list=raw_web3_list)
    stable_web3.init_web3("best", func=web3_callback_func)
    print(stable_web3.web3())
    print(stable_web3.web3_url())
    time.sleep(10)
    stable_web3.check_stable_web3(func=web3_callback_func)
    print("=========================================")
    print(stable_web3.web3())
    print(stable_web3.web3_url())
    time.sleep(10)
    print("===========================")
    abc = stable_web3.get_best_stable_web3(func=web3_callback_func)
    print(abc.web3)
    print(abc.rpc)
