import signal
import time

from example import raw_web3_list, web3_callback_func
from stable_ethereum_rpc.stable_web3.available_stable_web3 import AvailableStableWeb3


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
    print(f"rpc: {stable_web3.web3_entity().provider_url}")
    stable_web3.run_job(trigger="interval", args=[], seconds=30, max_instances=2)
    signal.pause()
