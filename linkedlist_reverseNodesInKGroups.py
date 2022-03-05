"""
Given a linked list l, reverse its nodes k at a time and return the modified list.
k is a positive integer that is less than or equal to the length of l.
If the number of nodes in the linked list is not a multiple of k,
then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example

For l = [1, 2, 3, 4, 5] and k = 2, the output should be
reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];
For l = [1, 2, 3, 4, 5] and k = 1, the output should be
reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].
"""
def reverseNodesInKGroups(l, k):
    if not l or k <= 1:
        return l
        
    new = []
    while l:
        new.append(l)
        l = l.next
    
    for i in range(len(new) // k):
        start = k * i
        end = k * (i + 1)
        new = new[:start] + list(reversed(new[start:end])) + new[end:]
        
    for i in range(len(new) - 1):
        new[i].next = new[i+1]
    new[-1].next = None
    
    return new[0]
