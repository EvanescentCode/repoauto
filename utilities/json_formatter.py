import json
from enum import Enum
from pathlib import PurePath
from typing import TypeVar
from dacite import Config, from_dict

T = TypeVar("T")


def _open_json(path: str | PurePath, encoding: str = 'utf-8') -> dict | list[dict]:
    with open(path, encoding=encoding) as file:
        return json.load(file)


def _make_dict_from_json(data_class: type[T], data: dict | list[dict]) -> T:
    return from_dict(data_class=data_class, data=data, config=Config(cast=[Enum], strict=True))


def load_test_data(dataclass: type[T], path: str | PurePath) -> T:
    return _make_dict_from_json(data_class=dataclass, data=_open_json(path))
