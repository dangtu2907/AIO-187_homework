def dem_chu(word):
    demchu = {}
    for letter in word:
        if letter in demchu:
            demchu[letter] += 1
        else:
            demchu[letter] = 1
    return demchu
word = str(input())
res = dem_chu(word)
print(res)
