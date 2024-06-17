num_list = list(map(int, input().split()))
k = int(input())
start_indexes = list(range(0, len(num_list)-k+1))
end_indexes = list(range(k, len(num_list)+1))

res = []

for start_index, end_index in zip(start_indexes, end_indexes): 
    sub_list = num_list[start_index: end_index]
    res.append(max(sub_list))

print(res)

