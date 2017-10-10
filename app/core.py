import re


def danify(text):
    return ' '.join(words(text))


def words(text):
    return filter(
        bool,
        [word.strip() for word in text.replace('\n', ' ').split()]
    )
