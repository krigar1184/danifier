import re


def danify(text):
    return ' '.join(words(text))


def words(text):
    words = text.split(' ')
    return words


def apply_rule(rule):
    return filter(
        bool,
        [word.strip() for word in text.replace('\n', ' ').split()]
    )
