#!/usr/bin/python3
8-multiple_returns.py

 """Returns a tuple with the length of a string and its first character."""
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        sen_len = len(sentence)
    else:
        sen_len = 0
    return (sen_len, sentence if not sentence else sentence[:1])

