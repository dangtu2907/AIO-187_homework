file_path = 'D:\\GITHUB\\AIO-187_homework-week2\\P1_data.txt' 

counter = {}

with open(file_path, 'r') as file:
    for line in file: 
        words = line.split()
        for word in words: 
            if word in counter: 
                counter[word] += 1 
            else: 
                counter[word] = 1 

print(counter)
