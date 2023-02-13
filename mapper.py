#!/usr/bin/env python
'''Mapper for vote counting system'''

import sys

PARTIES = ("LABOUR", "PDP", "APC", "REPUBLICAN", "DEMOCRATIC")

def is_valid_vote(vote: str) -> bool:
    return vote in PARTIES

def execute_mapper():
    for line in sys.stdin:
        votes = line.strip().split()
        for vote in votes:
            if is_valid_vote(vote):
                print("%s$%s".format(vote, 1))


if __name__ == "__main__":
    execute_mapper()