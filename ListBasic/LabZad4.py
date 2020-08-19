numbers = input().split(", ")
beggars = int(input())

output = [0]*beggars
for beggar in range(beggars):
    for i in range(beggar,len(numbers),beggars):
        output[beggar]+=int(numbers[i])
print(output)