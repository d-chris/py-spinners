from spinners.errors import ValidationError, ValidationSpinnerError
from spinners.future import Spinners as FutureSpinners
from spinners.register import register_spinner
from spinners.spinners import Spinners as LegacySpinners

register_spinner(LegacySpinners)

Spinners = FutureSpinners.load_spinners()


__all__ = [
    "Spinners",
    "register_spinner",
    "ValidationSpinnerError",
    "ValidationError",
    "LegacySpinners",
]
