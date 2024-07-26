import enum
from typing import Any


class ValidationError(TypeError):
    pass


class ValidationSpinnerError(ValidationError):
    pass


class ValidationObjectError(ValidationError):
    pass


class BaseSpinners:
    """
    BaseClass for Spinners to hold multiple Enums in a single class
    """

    _enums = []

    @classmethod
    def insert(cls, index: int, enum: enum.Enum) -> None:
        cls._validate_enum(enum)
        cls._enums.insert(index, enum)

    @classmethod
    def append(cls, enum: enum.Enum) -> None:
        cls._validate_enum(enum)
        cls._enums.append(enum)

    @classmethod
    def _validate_enum(cls, obj: enum.Enum) -> bool:
        """
        Check if an object is an Enum and has all the required attributes to be a
        Spinner.

        Raises 'ValidationSpinnerError' if the object fails the requirements.
        """
        if not issubclass(obj, enum.Enum):
            raise ValidationSpinnerError(f"{obj} must be an 'enum.Enum'")

        return True

    @classmethod
    def _validate_object(cls, obj: Any) -> bool:
        if not isinstance(obj, dict):
            raise ValidationObjectError(f"{obj} must be a 'Dict'")

        return True


__all__ = [
    "BaseSpinners",
    "ValidationError",
    "ValidationSpinnerError",
    "ValidationObjectError",
]
