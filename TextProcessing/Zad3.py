text = input().split("\\")

text1 = text[-1].split(".")

print(f"File name: {text1[0]}")
print(f"File extension: {text1[1]}")