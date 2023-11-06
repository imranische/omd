import pytest
from morse import decode

@pytest.mark.parametrize(
    "source_string, result",
    [
        ('.--. -.-- - .... --- -.', 'PYTHON'),
        ('... --- ...', 'SOS'),
        ('..   .-- .- -. -   - ---   ... .-.. . . .--.', 'IWANTTOSLEEP_bla_bla_bla')
    ]
)
def test_decode(source_string, result):
    assert decode(source_string) == result


if __name__ == '__main__':
    test_decode()

