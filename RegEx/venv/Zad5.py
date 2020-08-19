import re
pattern = r"[>]{2}([\w]+)[<]{2}([\d]+[\.][\d]+|[\d]+)[!]([\d]+)"

my_list = []
while True:
    text = input()
    if text == "Purchase":
        break
    match = re.findall(pattern, text)
    if match != []:
        my_list.extend(match)

print("Bought furniture:")
total_money_spend = 0
for each in my_list:
    print(each[0])
    total_money_spend += float(each[1])*float(each[2])
print(f"Total money spend: {total_money_spend:.2f}")


