from spinners.codepage import get_codepage


def test_codepage():
    assert isinstance(get_codepage(), str)
