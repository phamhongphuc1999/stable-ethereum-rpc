from typing import List, Dict

from stable_ethereum_rpc.web3_list.web3_entity import SimpleWeb3Entity, Web3Entity
from stable_ethereum_rpc.web3_measure import Web3Measure


class Web3List:
    def __init__(self, chain_id: int, web3_list: List[SimpleWeb3Entity or str], **kwargs):
        self.chain_id = chain_id
        self._list: Dict[str, Web3Entity] = {}
        max_timestamp = kwargs.get("max_timestamp")
        self._measure = Web3Measure(chain_id, max_timestamp)
        for web3_item in web3_list:
            if isinstance(web3_item, str):
                self.add_web3(SimpleWeb3Entity(web3_item, "http"))
            else:
                self.add_web3(web3_item)

    def get_sufficient_web3(self, **kwargs) -> Web3Entity or None:
        web3_keys = list(self._list.keys())
        _len = len(web3_keys)
        start_index: int = kwargs.get("start_index")
        provider_url: str = kwargs.get("provider_url")
        web3_callback_func = kwargs.get("func")
        if provider_url:
            start_index = web3_keys.index(provider_url)
        elif start_index is None or start_index >= _len:
            start_index = 0
        counter = start_index
        check = True
        result = self._list[web3_keys[start_index]]
        while check:
            _provider_url = web3_keys[counter]
            _web3_entity = self._list[_provider_url]
            measure_param = self._measure.measure(_web3_entity)
            if callable(web3_callback_func):
                web3_callback_func(_web3_entity, measure_param)
            if measure_param["isOk"]:
                result = _web3_entity
                check = False
            else:
                if counter < _len - 1:
                    counter += counter
                else:
                    counter = 0
                if counter == start_index:
                    check = False
                    result = None
        return result

    def get_best_web3(self, **kwargs) -> Web3Entity:
        web3_callback_func = kwargs.get("func")
        web3_value = list(self._list.values())
        _result: Web3Entity = web3_value[0]
        _temp_result = self._measure.measure(_result)
        _measure_param = _temp_result["result"]
        if callable(web3_callback_func):
            web3_callback_func(_result, _temp_result)
        for web3_item in web3_value[1:]:
            temp_measure = self._measure.measure(web3_item)
            if callable(web3_callback_func):
                web3_callback_func(web3_item, temp_measure)
            if temp_measure["isOk"]:
                if temp_measure["result"] < _measure_param:
                    _result = web3_item
                    _measure_param = temp_measure["result"]
        return _result

    def add_web3(self, web3_item: SimpleWeb3Entity, upsert=False) -> bool:
        provider_url = web3_item.provider_url
        rpc_type = web3_item.rpc_type
        is_exists = provider_url in self._list
        if upsert or (not is_exists):
            _temp = Web3Entity(provider_url, rpc_type, self.chain_id)
            self._list[provider_url] = _temp
            return True
        else:
            current_entity = self._list[provider_url]
            current_rpc_type = current_entity.rpc_type
            if current_rpc_type == rpc_type:
                return False
            else:
                _temp = Web3Entity(provider_url, rpc_type, self.chain_id)
                self._list[provider_url] = _temp
                return True

    def remove_web3(self, provider_url: str):
        if provider_url in self._list:
            del self._list[provider_url]
            return True
        return False
