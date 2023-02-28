import time

from example import raw_web3_list, web3_callback_func
from stable_ethereum_rpc.stable_web3.multiple_stable_web3 import MultipleStableWeb3


if __name__ == "__main__":
    multiple_web3 = MultipleStableWeb3(web3_list=raw_web3_list, func=web3_callback_func)
    stable_list = multiple_web3.web3_entities()
    for item in stable_list:
        print(f"rpc: {item.provider_url}")
    time.sleep(10)
    print("Set best web3========================================")
    result1 = multiple_web3.set_best_web3(func=web3_callback_func)
    rpc_list = result1["rpc"]
    current_rpc_list = result1["currentRpc"] if "currentRpc" in result1 else []
    print("RPC-------------------")
    for item in rpc_list:
        print(f"rpc: {item.provider_url}")
    if len(current_rpc_list) > 0:
        for item in current_rpc_list:
            print(f"old rpc: {item.provider_url}")
    time.sleep(10)
    print("Set sufficient web3=========================================")
    result2 = multiple_web3.set_sufficient_web3(func=web3_callback_func)
    rpc_list = result1["rpc"]
    current_rpc_list = result1["currentRpc"] if "currentRpc" in result1 else []
    print("RPC-------------------")
    for item in rpc_list:
        print(f"rpc: {item.provider_url}")
    if len(current_rpc_list) > 0:
        for item in current_rpc_list:
            print(f"old rpc: {item.provider_url}")
