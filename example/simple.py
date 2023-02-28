import time

from example import raw_web3_list, web3_callback_func
from stable_ethereum_rpc.stable_web3 import StableWeb3

if __name__ == "__main__":
    stable_web3 = StableWeb3(web3_list=raw_web3_list, func=web3_callback_func)
    print(f"rpc: {stable_web3.web3_entity().provider_url}")
    time.sleep(10)
    print("Set best web3=========================================")
    result1 = stable_web3.set_best_web3(func=web3_callback_func)
    _message = f"RPC: {result1['rpc'].provider_url}"
    if "currentRpc" in result1:
        _message += f", Current RPC: {result1['currentRpc'].provider_url}"
    print(_message)
    time.sleep(10)
    print("set sufficient web3=========================================")
    result = stable_web3.set_sufficient_web3(func=web3_callback_func)
    _message = f"RPC: {result['rpc'].provider_url}"
    if "currentRpc" in result:
        _message += f", Current RPC: {result['currentRpc'].provider_url}"
    print(_message)
