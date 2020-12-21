"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""
def allLongestStrings(inputArray):
    longest = max(map(len, inputArray))
    return [x for x in inputArray if len(x) == longest]
