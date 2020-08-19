int_list = input().split()
n = int(input())

temp_list=[int(i) for i in int_list]
num_to_remove = ""

for i in range(n):
    temp_list.sort(reverse=True)
    num_to_remove=temp_list.pop()
    # print(num_to_remove)
    int_list.remove(str(num_to_remove))

int_list=[int(i) for i in int_list]
print(int_list)
