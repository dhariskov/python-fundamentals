income = float(input())
months = int(input())
sum_needed = float(input())

save_percent = ((income - sum_needed - income*0.3)/income)*100
save_money = income - sum_needed - income*0.3
print(f"She can save {save_percent:.2f}%")
print(f"{save_money*months:.2f}")