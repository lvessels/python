"""
You're given 2 huge integers represented by linked lists.
Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits.
The represented number might have leading zeros.
Your task is to add up these huge integers and return the result in the same format.

Example

For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
addTwoHugeNumbers(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.
"""
def addTwoHugeNumbers(a, b):
    a_r = reverse_lst(a)
    b_r = reverse_lst(b)
    carry = 0
    new = None
    prev = None
    
    while a_r or b_r:
        c, carry = add(a_r, b_r,carry)
        if prev:
            prev.next = c
            prev = c
        if new is None:
            new = c
            prev = c
        if a_r:
            a_r = a_r.next
        if b_r:
            b_r = b_r.next
    if carry:
        c = ListNode(carry)
        prev.next = c
    return reverse_lst(new)
    
def reverse_lst(l):
    p,c = None, l
    while c is not None:
        tmp = c
        c = c.next
        tmp.next = p
        p = tmp
    return p
    
def add(f, s, carry):
    f_val = f.value if f else 0
    s_val = s.value if s else 0
    tmp = f_val + s_val + carry
    return ListNode(tmp % 10000), tmp // 10000
