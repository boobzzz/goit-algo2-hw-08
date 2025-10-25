def find_min_max(numbers):
    if numbers[0] == numbers[len(numbers) - 1]:
        return (numbers[0], numbers[0])

    if len(numbers) - 1 == 1:
        if numbers[0] < numbers[1]:
            return (numbers[0], numbers[1])
        else:
            return (numbers[1], numbers[0])

    mid = len(numbers) // 2
    min1, max1 = find_min_max(numbers[:mid])
    min2, max2 = find_min_max(numbers[mid:])

    final_min = min(min1, min2)
    final_max = max(max1, max2)

    return (final_min, final_max)


print(find_min_max([5, 2, 4, 3, 13, 9, 7]))
