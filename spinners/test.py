# decorator.py


def enum_class(priority=None):
    """
    Decorator to mark an enum class and register it in the base class.
    """

    def decorator(cls):
        BaseClass.register_enum(cls, priority)
        return cls

    return decorator


class BaseClass:
    _registered_enums = {}

    @classmethod
    def register_enum(cls, enum_cls, priority=None):
        """
        Register an enum class.
        """
        key = priority if priority is not None else enum_cls.__name__
        cls._registered_enums[key] = enum_cls

    @classmethod
    def get_registered_enums(cls):
        """
        Get all registered enum classes.
        """
        return cls._registered_enums


# Example usage
from enum import Enum


@enum_class(priority="high_priority_enum")
class MyEnum(Enum):
    VALUE1 = 1
    VALUE2 = 2


# Verify registration
print(BaseClass.get_registered_enums())
