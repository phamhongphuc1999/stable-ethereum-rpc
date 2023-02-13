from typing import List

from stable_ethereum_rpc.web3_entity import SimpleWeb3Entity, Web3Entity
from stable_ethereum_rpc.web3_list import BaseWeb3List


def _sort(item):
    return item["measure"]["result"]


def _map(item):
    return item["item"]


class MultipleWeb3List(BaseWeb3List):
    def __init__(self, chain_id: int, web3_list: List[SimpleWeb3Entity or str], **kwargs):
        super().__init__(chain_id, web3_list, **kwargs)
        _size = kwargs.get("size")
        self.selected_size = _size if _size else 2

    def get_sufficient_web3(self, **kwargs) -> List[Web3Entity] or None:
        web3_keys = list(self._list.keys())
        return []

    def get_best_web3(self, **kwargs) -> List[Web3Entity] or None:
        measure_data = self.measure_all(**kwargs)
        data = list(measure_data.values())
        raw_result = []
        for item in data:
            if item["measure"]["isOk"]:
                raw_result.append(item)
        raw_result.sort(key=_sort)
        return list(map(_map, raw_result[0 : self.selected_size]))
