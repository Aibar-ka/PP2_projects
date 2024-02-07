def calculate_running_average(numbers):
    running_average = []
    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1
        average = total / count
        running_average.append(average)

    return running_average

series = [1, 2, 3, 4, 5, 6, 7]
result = calculate_running_average(series)
print(result)
