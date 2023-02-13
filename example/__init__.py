from stable_ethereum_rpc.web3_entity import Web3Entity

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
