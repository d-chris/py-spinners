import enum
from typing import List, Set

from spinners.codepage import *
from spinners.enums import *
from spinners.errors import *


class Spinners(EnumSpinners):
    @classmethod
    def _validate_enum(cls, obj: enum.Enum) -> bool:
        valid = super()._validate_enum(obj)

        try:
            for spinner in obj._member_map_.keys():
                spin = getattr(obj, spinner).value

                if not isinstance(spin, dict):
                    raise ValidationSpinnerError(f"{spin=} must be of type 'dict'")

                interval = spin["interval"]

                if not isinstance(interval, int) or interval <= 0:
                    raise ValidationSpinnerError(
                        f"{interval=} must be of type 'int' and greater than 0"
                    )

                frames = spin["frames"]

                if not isinstance(frames, list):
                    raise ValidationSpinnerError(f"{frames=} must be of type 'list'")

                if not len(frames):
                    raise ValidationSpinnerError(f"{frames=} must not be empty")

                for frame in frames:
                    if not isinstance(frame, str):
                        raise ValidationSpinnerError(f"{frame=} must be of type 'str'")

        except AttributeError as e:
            raise ValidationSpinnerError(f"{spinner=} must be of type 'dict'") from e
        except KeyError as e:
            raise ValidationSpinnerError(f"{e=} must be a key in 'spin'") from e

        return valid and True

    def spinners(self, codepage: str = None) -> List[str]:
        try:
            enums = self._member_map_.keys()
        except AttributeError:
            return []

        if codepage is None:
            return list(enums)

        def encoder():
            for enum in enums:
                spin = getattr(self, enum).value

                try:
                    for frame in spin["frames"]:
                        frame.encode(codepage)
                except UnicodeEncodeError as e:
                    continue

                yield enum

        return list(encoder())


def spinners_guaranteed() -> Set[str]:
    return set(Spinners().spinners(get_codepage()))


def spinners_available() -> Set[str]:
    return set(Spinners().spinners(None))


__all__ = [
    "Spinners",
    "spinners_guaranteed",
    "spinners_available",
]
