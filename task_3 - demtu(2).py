file_path = 'D:\GITHUB\AIO-187_homework-week2\P1_data.txt' 

with open(file_path, 'r') as file:
    for lines in file: 
        words = lines.split()
        counter = {}
        for word in words: 
            if word in counter: 
                counter[word] += 1 
            else: 
                counter[word] = 1 

print(counter)