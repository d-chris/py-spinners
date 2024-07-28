import enum

import pytest

from spinners.enums import EnumSpinners


@pytest.fixture
def _EnumSpinners(spinners):

    EnumSpinners._enums.clear()

    EnumSpinners.append(spinners)

    yield EnumSpinners()

    EnumSpinners._enums.clear()


@pytest.fixture(
    params=[
        "line",
        "dots",
    ]
)
def _enum(request):
    return request.param


def test_enum_attributes(
    _EnumSpinners: EnumSpinners,
    spinners: enum.Enum,
    _enum: str,
) -> None:

    assert getattr(_EnumSpinners, _enum) == getattr(spinners, _enum)


def test_enum_item(
    _EnumSpinners: EnumSpinners, spinners: enum.Enum, _enum: str
) -> None:
    assert _EnumSpinners[_enum] == spinners[_enum]


def test_enum_member_names(_EnumSpinners: EnumSpinners, spinners: enum.Enum) -> None:

    assert _EnumSpinners._member_names_ == spinners._member_names_


def test_enum_member_map(_EnumSpinners: EnumSpinners, spinners: enum.Enum) -> None:

    assert _EnumSpinners._member_map_ == spinners._member_map_


def test_enum_value2member_map(
    _EnumSpinners: EnumSpinners, spinners: enum.Enum
) -> None:

    assert _EnumSpinners._value2member_map_ == spinners._value2member_map_


def test_enum_unhashable_values(
    _EnumSpinners: EnumSpinners, spinners: enum.Enum
) -> None:

    assert _EnumSpinners._unhashable_values_ == spinners._unhashable_values_
