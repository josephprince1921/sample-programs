numbers=[4,8,9,7,5]
for i in range(len(numbers)):
    min = i 
    for j in range(i+1, len(numbers)):
        if numbers[j]< numbers[min]:
            min = j 
    numbers[i],numbers[min]=numbers[min],numbers[i]
print(numbers)    