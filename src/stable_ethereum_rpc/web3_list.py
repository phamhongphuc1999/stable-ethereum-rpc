from web3 import Web3

from stable_ethereum_rpc.utils import create_web3_provider
from stable_ethereum_rpc.web3_measure import Web3Measure


class Web3Entity:
    def __init__(self, web3: Web3, rpc_str: str, _type: str, chain_id: int):
        self.web3 = web3
        self.rpc = rpc_str
        self.type = _type
        self.chain_id = chain_id


class Web3List:
    def __init__(self, web3_list: list, chain_id: int, max_timestamp: int):
        self.chain_id = chain_id
        self._list: {str: Web3Entity} = {}
        for _web3 in web3_list:
            self.add_web3(_web3["url"], _web3["type"])
        self._measure = Web3Measure(chain_id, max_timestamp)
        self._stable_web3: Web3Entity = self._get_best_stable_web3()

    def web3(self):
        return self._stable_web3.web3

    def web3_url(self):
        return self._stable_web3.rpc

    def _get_best_stable_web3(self) -> Web3Entity:
        web3_value = list(self._list.values())
        _result = web3_value[0]
        _measure_param = self._measure.test_web3(web3_value[0].web3)["result"]
        for web3_item in web3_value[1:]:
            temp_measure = self._measure.test_web3(web3_item.web3)
            if temp_measure["isOk"]:
                if temp_measure["result"] < _measure_param:
                    _result = web3_item
                    _measure_param = temp_measure["result"]
        return _result

    def add_web3(self, provider_url: str, _type: str, upsert=False) -> bool:
        is_already_exists = provider_url in self._list
        if upsert or (not is_already_exists):
            provider_web3 = create_web3_provider(provider_url, _type)
            self._list[provider_url] = Web3Entity(provider_web3, provider_url, _type, self.chain_id)
            return True
        else:
            current_entity = self._list[provider_url]
            current_type = current_entity.type
            if current_type == _type:
                return False
            else:
                provider_web3 = create_web3_provider(provider_url, _type)
                self._list[provider_url] = Web3Entity(provider_web3, provider_url, _type, self.chain_id)

    def remove_web3(self, provider_url: str) -> bool:
        if provider_url in self._list:
            del self._list[provider_url]
            return True
        else:
            return False
