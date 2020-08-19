quota = int(input())

counter_price_get_money = 0
counter_price_pay_money = 0
get_money = 0
pay_money  = 0
fish_count = 0
for i in range(1,quota+1):
    fish_name = input()
    if fish_name == "Stop":
        break
    fish_weight = float(input())
    fish_count+=1
    counter_price_get_money=0
    counter_price_pay_money=0
    for j in range (0 , len(fish_name)):
        if i%3==0:
            counter_price_get_money+=ord(fish_name[j])
        else:
            counter_price_pay_money+=ord(fish_name[j])
    get_money = get_money + (counter_price_get_money / fish_weight)
    pay_money = pay_money + (counter_price_pay_money / fish_weight)
if fish_name!="Stop":
    print("Lyubo fulfilled the quota!")
if get_money - pay_money>=0:
    print(f"Lyubo's profit from {fish_count} fishes is {(get_money - pay_money):.2f} leva.")
else:
    print(f"Lyubo lost {(pay_money-get_money):.2f} leva today.")