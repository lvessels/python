"""
Given a singly linked list of integers, determine whether or not it's a palindrome.

Note: in examples below and tests preview linked lists are presented as arrays
just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

For l = [0, 1, 0], the output should be
isListPalindrome(l) = true;

For l = [1, 2, 2, 3], the output should be
isListPalindrome(l) = false.
"""
def isListPalindrome(l):
    if not l:
        return True
    l = convert(l)
    return sum([1 for x,y in zip(l, reversed(l)) if x != y]) == 0

def convert(t):
    lst = list()
    while t.next is not None:
        lst.append(t.value)
        t = t.next
    lst.append(t.value)
    return lst
