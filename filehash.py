#!/usr/bin/env python3
"""
This module hashes JSON files with the SHA256 Crytography Algorithm
"""
import hashlib
import sys

file_name = sys.argv[1]

hasher = hashlib.sha256()
with open(file_name, 'rb') as f:
    buf = f.read()
    hasher.update(buf)
    print(hasher.hexdigest())
