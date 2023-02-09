from stable_ethereum_rpc.stable_web3 import StableWeb3

raw_web3_list = [
    {"url": "https://bsc-dataseed.binance.org", "type": "http"},
    {"url": "https://bsc-dataseed1.binance.org", "type": "http"},
    {"url": "https://bsc-dataseed1.defibit.io", "type": "http"},
    {"url": "https://bsc-dataseed2.defibit.io", "type": "http"},
    {"url": "https://bsc-dataseed1.ninicoin.io", "type": "http"},
    {"url": "https://bsc-dataseed2.ninicoin.io", "type": "http"},
]

if __name__ == "__main__":
    stable_web3 = StableWeb3(raw_web3_list=raw_web3_list)
    print(stable_web3.web3())
    print(stable_web3.web3_url())
