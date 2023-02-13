from stable_ethereum_rpc.web3_entity import Web3Entity
from stable_ethereum_rpc.web3_list.multiple_web3_list import MultipleWeb3List

raw_web3_list = [
    "https://bsc-dataseed234567.ninicoin.io",
    "https://bsc-dataseed.binance.org",
    "https://bsc-dataseed1.binance.org",
    "https://bsc-dataseed1.defibit.io",
    "https://bsc-dataseed2.defibit.io",
    "https://bsc-dataseed1.ninicoin.io",
    "https://bsc-dataseed2.ninicoin.io",
]


def web3_callback_func(web3: Web3Entity, params: object):
    print(f"web3: {web3.provider_url}, result: {params}")


if __name__ == "__main__":
    # multiple_web3 = MultipleWeb3List(web3_list=raw_web3_list, func=web3_callback_func)
    pass
