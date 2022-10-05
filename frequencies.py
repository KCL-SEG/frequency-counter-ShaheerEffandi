"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if(not(str(item) in frequencies)):
            frequencies[str(item)] = 1
        else:
            frequencies[str(item)] += 1

    return frequencies
