def second_largest(lists):

    largest = lists[0]
    second = lists[0]

    for list in lists:
        if list > largest:
            second = largest
            largest = list
        elif largest > list > second:
            second = list
    return second
print(second_largest([15, 15]))
