def delete(list_of_words, index):
    if -1 <= index <= len(list_of_words) - 2:
        list_of_words.pop(index + 1)
    return list_of_words


def swap(list_of_words, word1, word2):
    if word1 in list_of_words and word2 in list_of_words:
        index_word1 = list_of_words.index(word1)
        index_word2 = list_of_words.index(word2)
        list_of_words[index_word1], list_of_words[index_word2] = list_of_words[index_word2], list_of_words[index_word1]
    return list_of_words


def put(list_of_words, word, index):
    if 1 <= index <= len(list_of_words) + 1:
        list_of_words.insert(index - 1, word)
    return list_of_words


def sort(list_of_words):
    list_of_words.sort(reverse=True)
    return list_of_words


def replace(list_of_words, word1, word2):
    if word2 in list_of_words:
        list_of_words[list_of_words.index(word2)] = word1
    return list_of_words


words = input().split(" ")
temp = []
while True:
    command = input()
    if command == "Stop":
        break
    temp = command.split(" ")
    if temp[0] == "Delete":
        words = delete(words, int(temp[1]))
    elif temp[0] == "Swap":
        words = swap(words, temp[1], temp[2])
    elif temp[0] == "Put":
        words = put(words, temp[1], int(temp[2]))
    elif temp[0] == "Sort":
        words = sort(words)
    elif temp[0] == "Replace":
        words = replace(words, temp[1], temp[2])

for each in words:
    print(each, end=" ")
