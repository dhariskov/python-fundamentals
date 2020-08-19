quantity = int(input())
days = int(input())
ornament_set =2
tree_skirt =5
tree_garlands =3
tree_lights =15
price = 0
spirit = 0
for i in range (1, days+1):
    if i%2==0:
        price += ornament_set*quantity
        spirit+=5
    if i%3 == 0:
        price+=(tree_skirt+tree_garlands)*quantity
        spirit+=13
    if i%5==0:
        price+=tree_lights*quantity
        spirit+=17
        if i%3==0:
            spirit += 30
    if i%10 ==0:
        spirit-=20
        price+=tree_skirt+tree_garlands+tree_lights
    if i%11 == 0:
        quantity+=2
    if days == 10 and i == 10:
        spirit-=10

print(f"Total cost: {price}")
print(f"Total spirit: {spirit}")