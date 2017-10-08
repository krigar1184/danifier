import pytest

from app.core import danify


@pytest.mark.parametrize(('input_data', 'expected'), [
    ('mann', 'mand'),
    ('bok', 'bog'),
    ('å', 'at'),
    ('at', 'at')
])
def test_danify(input_data, expected):
    assert danify(input_data) == expected
