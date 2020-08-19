campaign_last = int(input())
cheffs_number = int(input())
cake_number = int(input())
goff_number = int(input())
pan_number = int(input())

cake_total = campaign_last * cheffs_number * cake_number * 45
goff_total = campaign_last * cheffs_number * goff_number * 5.8
pan_total = campaign_last * cheffs_number * pan_number * 3.20

# print(cake_total)
# print(goff_total)
# print(pan_total)
total_money= (cake_total + goff_total + pan_total) - (cake_total + goff_total + pan_total)*(1/8)

print(f"{total_money:.2f}")
