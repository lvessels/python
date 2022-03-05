"""
Given two singly linked lists sorted in non-decreasing order, your task is to merge them.
In other words, return a singly linked list,
also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
"""
def mergeTwoLinkedLists(l1, l2):
    new = ListNode(0)
    tmp = new
    while True:
        if l1 is None and l2 is None:
            break
        elif l1 is None:
            tmp.next = l2
            break
        elif l2 is None:
            tmp.next = l1
            break
        else:
            m = 0
            if l1.value < l2.value:
                m = l1.value
                l1 = l1.next
            else:
                m = l2.value
                l2 = l2.next
            newM = ListNode(m)
            tmp.next = newM
            tmp = tmp.next
    return new.next 
