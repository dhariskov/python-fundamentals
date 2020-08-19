word = input()
word_list = []
result = ""
for i in range(len(word)):
    word_list.append(word[i])

for each in range(len(word_list) - 1):
    if not (word_list[each] == word_list[each + 1]):
        result += word_list[each]

result += word_list[-1]

print(result)
