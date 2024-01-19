#!/usr/bin/python3
def multiple_returns(sentence):
    return [len(sentence), sentence if len(sentence) > 0 else None]
