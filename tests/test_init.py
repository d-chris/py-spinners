from spinners import Spinners
from spinners.future import Spinners as FutureSpinners


def test_spinners():
    assert type(Spinners) == FutureSpinners
