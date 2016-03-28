#!/usr/bin/env python3
"""Retrieve and print document frooma url
Usage:
    python3 request.py <URL>
"""
from urllib.request import urlopen
import sys

def fetch_word(url):
    """Fetch a list of words from the url
    Args:
        url: The url of a utf-8 text document
    Return:
        A string of document words
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_split = line.decode('utf-8').split()
            for word in line_split:
                story_words.append(word)
    return story_words

def print_words(items):
    for item in items:
        print(item)

def main(url):
    word = fetch_word(url)
    print_words(word)

# implementation to run python as a script
if __name__ == '__main__':
    main(sys.argv[1])
