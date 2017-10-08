import pytest

from app.core import danify, words


@pytest.mark.parametrize(('input_data', 'expected'), [
    ('mann', 'mand'),
    ('bok', 'bog'),
    ('å', 'at'),
    ('at', 'at')
])
def test_danify(input_data, expected):
    assert danify(input_data) == expected


@pytest.mark.parametrize(('input_data', 'expected'), [
    ('three words here', ['three', 'words', 'here']),
    ('text, with, commas', ['text', 'with', 'commas']),
    ('    text-with  -spaces    ', ['text-with', 'spaces'])
])
def test_words(input_data, expected):
    assert words(input_data) == expected
