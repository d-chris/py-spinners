import pytest

from spinners.enums import EnumSpinners


@pytest.fixture
def spin(spinners):
    spin = EnumSpinners()

    spin.append(spinners)

    yield spin

    spin._enums.clear()


@pytest.mark.parametrize(
    "enum",
    [
        "line",
        "dots",
    ],
)
def test_enum_attributes(spin, spinners, enum):

    spin.append(spinners)

    assert getattr(spin, enum) == getattr(spinners, enum)
