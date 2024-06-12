def max_number(num_list, k):
    if not num_list or k == 0:
        return []

    result = []
    for i in range(len(num_list) - k + 1):
        window = num_list[i:i + k]
        window_max = max(window)
        result.append(window_max)
    return result


num_list = list(map(int, input().split()))
k = 3
b = max_number(num_list, k)
print(b)
