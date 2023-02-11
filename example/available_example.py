import signal
import time

from stable_ethereum_rpc.stable_web3.available_stable_web3 import AvailableStableWeb3
from stable_ethereum_rpc.web3_list import Web3Entity

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


def available_callback_func(params):
    current_timestamp = time.time()
    _message = f"RPC: {params['rpc'].provider_url}"
    if "currentRpc" in params:
        _message += f", Current RPC: {params['currentRpc'].provider_url}"
    print(f"message: {_message}, timestamp: {current_timestamp}")
    print("=============================================================")


if __name__ == "__main__":
    stable_web3 = AvailableStableWeb3(
        web3_list=raw_web3_list, func=web3_callback_func, callback_func=available_callback_func, job_mode="best"
    )
    print(f"rpc: {stable_web3.web3().provider_url}")
    stable_web3.run_job(trigger="interval", args=[], seconds=30, max_instances=2)
    signal.pause()
