import enum

import pytest

from spinners.base import BaseSpinners


@pytest.fixture(
    params=[
        BaseSpinners,
    ],
    ids=lambda cls: cls.__name__,
)
def classes(request):
    cls = request.param

    yield cls

    cls._enums.clear()


@pytest.fixture
def obj_spinners():
    return {
        "line": {
            "interval": 100,
            "frames": [
                "-",
                "\\",
                "|",
                "/",
            ],
        },
        "dots": {
            "interval": 80,
            "frames": [
                ".  ",
                ".. ",
                "...",
                "   ",
            ],
        },
    }


@pytest.fixture
def spinners(obj_spinners):
    return enum.Enum(
        "spinner",
        obj_spinners,
    )


@pytest.fixture(
    params=[
        {"none": None},
        {"line": {"interval": 0, "frames": ["-", "\\", "|", "/"]}},
        {"dots": {"interval": 80, "frame": [".  ", ".. ", "...", "   "]}},
        {"empty": {"interval": 100, "frames": []}},
        {"baloon": {"interval": "1", "frames": [".", "o", "O", "°"]}},
    ],
    ids=lambda e: list(e.keys())[0],
)
def obj_invalid_spinners(request):
    return request.param


def invalid_spinner(obj_invalid_spinners):
    return enum.Enum(
        "invalid_spinner",
        obj_invalid_spinners,
    )


@pytest.fixture(
    params=[list, dict, set],
)
def invalid_class(request):
    return request.param
