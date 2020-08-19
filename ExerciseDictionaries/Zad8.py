
my_dict = {}
while True:
    command = input()
    if command == "End":
        break
    command = command.split(" -> ")
    company_name = command[0]
    emp_id = command[1]
    if company_name not in my_dict:
        my_dict[company_name] = [emp_id]
    if emp_id not in my_dict[company_name]:
        my_dict[company_name].append(emp_id)

my_dict = dict(sorted(my_dict.items(), key=lambda x:x[0]))

for key, value in my_dict.items():
    print(key)
    for each in value:
        print(f"-- {each}")
