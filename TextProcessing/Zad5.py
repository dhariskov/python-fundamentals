text = input()
for ch in range(len(text)-1):
    if text[ch] == ":" and text[ch+1] != " ":
        print(text[ch] + text[ch+1])
