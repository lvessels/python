"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""
def commonCharacterCount(s1, s2):
    total = 0 
    s1_count = {k:s1.count(k) for k in s1}
    s2_count = {k:s2.count(k) for k in s2}
    for k,v in s1_count.items():
        if k in s2_count:
            total += min(s1_count[k], s2_count[k])
    return total
