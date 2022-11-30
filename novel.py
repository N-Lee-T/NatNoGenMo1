# create new function that will recognize sentences from files

import re
import sys


def find_sentences(some_words):
    """
    Uses re to match sentences in a text file
    Eventually will be modified to take open source novels as sys.argv
    :param some_words: text, in the form of sentences
    :return: dictionary where sentence : [list of words in sentence]
    """
    if not isinstance(some_words, str):
        return None
    wordlist = [word for word in re.findall("[A-Z].*?[.!?\"]", some_words, re.MULTILINE | re.DOTALL)]
    sentences = {}
    for num in range(len(wordlist)):
        sentences[wordlist[num]] = [word.strip('.,;:!?$*()-\"\'\\') for word in wordlist[num].split(' ')]
    return sentences

