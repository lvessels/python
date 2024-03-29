"""
You found two items in a treasure chest!
The first item weighs weight1 and is worth value1,
and the second item weighs weight2 and is worth value2.
What is the total maximum value of the items you can take with you,
assuming that your max weight capacity is maxW and you can't come back for the items later?

Note that there are only two items and you can't bring more than one item of each type,
i.e. you can't take two first items or two second items.

Example

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be
knapsackLight(value1, weight1, value2, weight2, maxW) = 10.
"""
def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 > maxW and weight2 > maxW:
        return 0
    elif weight1 + weight2 <= maxW:
        return value1 + value2
    elif weight1 <= maxW and weight2 <= maxW:
        return max(value1, value2)
    elif weight1 <= maxW and weight2 > maxW:
        return value1
    else:
        return value2
