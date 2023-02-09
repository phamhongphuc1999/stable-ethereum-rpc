from stable_ethereum_rpc.config import AppConfig, ChainId
from stable_ethereum_rpc.web3_list import Web3List


class StableWeb3:
    def __init__(self, **kwargs):
        chain_id = kwargs.get("chain_id")
        max_timestamp = kwargs.get("max_timestamp")
        if not chain_id:
            chain_id = ChainId.BSC_MAINNET
            max_timestamp = AppConfig.DEFAULT_NETWORK[chain_id]["maxTimestamp"]
        else:
            if chain_id not in AppConfig.DEFAULT_NETWORK:
                if not max_timestamp:
                    raise Exception("max_timestamp is not provide")
            else:
                if not max_timestamp:
                    max_timestamp = AppConfig.DEFAULT_NETWORK[chain_id]["maxTimestamp"]
        if chain_id not in AppConfig.DEFAULT_NETWORK:
            raise Exception(f"{chain_id} is not supported")
        self.chain_id = chain_id
        web3_list = kwargs.get("web3_list")
        raw_web3_list = kwargs.get("raw_web3_list")
        if web3_list:
            self._web3_list = web3_list
        elif raw_web3_list:
            self._web3_list = Web3List(raw_web3_list, chain_id, max_timestamp)
        else:
            raise Exception("Your web3 list is empty")

    def web3(self):
        return self._web3_list.web3()

    def web3_url(self):
        return self._web3_list.web3_url()

    def add_web3(self, provider_url: str, _type: str, upsert=False) -> bool:
        return self._web3_list.add_web3(provider_url, _type, upsert)

    def remove_web3(self, provider_url: str) -> bool:
        return self._web3_list.remove_web3(provider_url)