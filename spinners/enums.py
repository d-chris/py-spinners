import itertools
from typing import Any

from spinners.base import BaseSpinners, ValidationError


class EnumSpinners(BaseSpinners):
    """
    Wrapper class to register multiple Enum classes and access attributes from them.
    """

    def __init__subclass__(cls, **kwargs) -> None:
        raise NotImplementedError

    def __call__(self, name: str) -> Any:
        return self.__getitem__(name)

    def __getattr__(self, name):
        for enum in self._enums:
            try:
                return getattr(enum, name)
            except AttributeError:
                continue

    def __getitem__(self, name):
        for enum in self._enums:
            try:
                return enum[name]
            except KeyError:
                continue

    @property
    def _member_names_(self):
        return list(
            itertools.chain(
                self._enum._member_names_,
                *(enum._member_names_ for enum in self._enums),
            )
        )

    @property
    def _member_map_(self):
        return dict(
            itertools.chain(
                self._enum._member_map_.items(),
                *(enum._member_map_.items() for enum in self._enums),
            )
        )

    @property
    def _value2member_map_(self):
        return dict(
            itertools.chain(
                self._enum._value2member_map_.items(),
                *(enum._value2member_map_.items() for enum in self._enums),
            )
        )

    @property
    def _unhashable_values_(self):
        return set(
            itertools.chain(
                self._enum._unhashable_values_,
                *(enum._unhashable_values_ for enum in self._enums),
            )
        )


__all__ = [
    "EnumSpinners",
]
