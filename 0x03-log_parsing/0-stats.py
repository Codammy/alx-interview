#!/usr/bin/env python3
"""
script that reads stdin line by line and computes metrics
"""
import sys
import re


if __name__ == "__main__":
    count = 0
    while True:
        read_in = sys.stdin.readline()
        re.compile(read_in)

        