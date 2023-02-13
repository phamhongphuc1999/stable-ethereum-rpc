from typing import List

from stable_ethereum_rpc.config import ChainId, AppConfig
from stable_ethereum_rpc.web3_entity import SimpleWeb3Entity, Web3Entity
from stable_ethereum_rpc.web3_list.multiple_web3_list import MultipleWeb3List


class MultipleStableWeb3:
    def __init__(self, **kwargs):
        web3_list: MultipleWeb3List or List[SimpleWeb3Entity or str] = kwargs.get("web3_list")
        if not web3_list:
            raise Exception("web3_list in not found")
        if isinstance(web3_list, list):
            chain_id = kwargs.get("chain_id")
            max_timestamp = kwargs.get("max_timestamp")
            if not chain_id:
                chain_id = ChainId.BSC_MAINNET
                max_timestamp = AppConfig.DEFAULT_NETWORK[chain_id]["maxTimestamp"]
            else:
                if chain_id not in AppConfig.DEFAULT_NETWORK:
                    if not max_timestamp:
                        raise Exception("max_timestamp is not found")
                else:
                    if not max_timestamp:
                        max_timestamp = AppConfig.DEFAULT_NETWORK[chain_id]["maxTimestamp"]
            self.chain_id = chain_id
            self._web3_list = MultipleWeb3List(chain_id, web3_list, max_timestamp=max_timestamp)
        elif isinstance(web3_list, MultipleWeb3List):
            self._web3_list: MultipleWeb3List = web3_list
            self.chain_id = self._web3_list.chain_id
        mode = kwargs.get("mode")
        func = kwargs.get("func")
        if mode == "best":
            self._stable_web3: List[Web3Entity] = self._web3_list.get_best_web3(func=func)
        else:
            self._stable_web3: List[Web3Entity] = self._web3_list.get_sufficient_web3(func=func)

    def _init_best_web3(self, **kwargs):
        self._stable_web3 = self._web3_list.get_best_web3(**kwargs)

    def _init_sufficient_web3(self, **kwargs):
        self._stable_web3 = self._web3_list.get_sufficient_web3(**kwargs)

    def init_web3(self, mode, **kwargs):
        if mode == "best":
            self._init_best_web3(**kwargs)
        else:
            self._init_sufficient_web3(**kwargs)

    def web3(self):
        return self._stable_web3

    def add_web3(self, web3_item: SimpleWeb3Entity, upsert=False) -> bool:
        return self._web3_list.add_web3(web3_item, upsert)

    def remove_web3(self, provider_url: str) -> bool:
        return self._web3_list.remove_web3(provider_url)
