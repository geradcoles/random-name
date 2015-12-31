"""
Random Name Generator
"""
from collections import deque
import random

import importlib
import warnings

def fetch_words(list_name):
    """
    Returns a tuple of words from the word libraries contained here.
    """
    mod = importlib.import_module(
        '.lists.%s' % list_name, package='randomname')
    return mod.WORDS

def generate(wordlists, wordcount=1, separator=' '):
    """
    Given an iterable of wordlists to use, generates a random name.

    :param wordlists: a list of wordlists to use (from 'randomname.lists')
    :param int wordcount: number of words to generate
    :param str separator: a word separator to use (defaults to a single space)
    """
    wordlist = WordList()
    for wlist in wordlists:
        wordlist.add_words(fetch_words(wlist))
    name = []
    for _ in range(wordcount):
        name.append(wordlist.random_word())
    return separator.join(name)

def generate_human_name(male=True, female=True, separator=' '):
    """
    Generate a random American-sounding name like 'John Smith'.

    Gender can be selected by toggling male/female.
    """
    firstnames = WordList()
    if male:
        firstnames.add_words(fetch_words('names_male'))
    if female:
        firstnames.add_words(fetch_words('names_female'))
    lastnames = WordList(words=fetch_words('surnames_american'))
    names = []
    names.append(firstnames.random_word())
    names.append(lastnames.random_word())
    return separator.join(names)

def generate_hostname(wordcount=2, separator='-'):
    """
    Useful for generating machine hostnames. Uses a combination of descriptors
    and nouns to create interesting, easy to read names.

    Adjectives and actions will be used for all but the final word in the
    name, which will instead be comprised of animals, male/female names, and
    occupations.
    """
    words = []
    for _ in range(wordcount - 1):
        wl = WordList()
        wl.add_wordlist('adjectives')
        wl.add_wordlist('actions')
        wl.add_wordlist('personalities')
        wl.add_wordlist('visual_colors')
        wl.add_wordlist('visual_pattern')
        words.append(wl.random_word())

    wl = WordList()
    wl.add_wordlist('animals')
    wl.add_wordlist('occupations')
    wl.add_wordlist('fruit')
    wl.add_wordlist('mnemonic')
    words.append(wl.random_word())
    return separator.join(words).lower()

class WordList:

    def __init__(self, words=None):
        """
        Initialize the word list. Optionally pass a list of words to this
        constructor to pre-initialize the list.
        """
        if words is None:
            words = []
        self._words = deque(words)

    @classmethod
    def load_from_file(cls, filename):
        """
        Create a new WordList from the specified filename. Returns
        the WordList object.
        """
        wl = cls()
        wl.add_file(filename)
        return wl

    @property
    def words(self):
        """
        Returns a read-only tuple version of the entire wordlist
        """
        return tuple(self._words)

    def random_word(self):
        """
        Returns a random word from the list, as a string.
        """
        return random.choice(self._words)

    def add_words(self, words):
        """
        Given an iterable of words, add them to this list.
        """
        self._words.extend(words)

    def add_wordlist(self, listname):
        """
        Add words from one of the built-in wordlists (from randomname.lists)
        """
        self.add_words(fetch_words(listname))

    def add_file(self, filename):
        """
        Given a path to a file containing a word list (one word per line),
        load all the words into this WordList in an append-like fashion.
        """
        with open(filename, 'r') as fh:
            self._words.extend(fh.read().splitlines())
