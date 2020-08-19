string1 = input()
string2 = input()

for i in range(0,len(string1)):
    if string1[i] != string2[i]:
        for k in range(0,i+1):
            print(string2[k], end="")
        for j in range(i+1,len(string2)):
            print(string1[j], end="")
        print()