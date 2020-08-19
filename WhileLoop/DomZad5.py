import math

change = float(input())
change *= 100

count_levs_2 = change // 200
levs_1 = change % 200
count_levs_1 = levs_1 // 100
stotinki = levs_1 % 100
count_stotinki_50 = stotinki // 50
stotinki_20 = stotinki % 50
count_stotinki_20 = (stotinki_20) // 20
stotinki_10 = stotinki_20 % 20
count_stotinki_10 = stotinki_10 // 10
stotinki_5 = stotinki_10 % 10
count_stotinki_5 = stotinki_5 // 5
stotinki_2 = stotinki_5 % 5
count_stotinki_2 = stotinki_2 // 2
count_stotinki_1 = stotinki_2 % 2
# print(math.floor(count_levs_2))
# print(math.floor(count_levs_1))
# print(math.floor(count_stotinki_50))
# print(math.floor(count_stotinki_20))
# print(math.floor(count_stotinki_10))
# print(math.floor(count_stotinki_5))
# print(math.floor(count_stotinki_2))
# print(math.floor(count_stotinki_1))

print(math.floor(
    count_stotinki_1 + count_stotinki_2 + count_stotinki_5 + count_stotinki_10 + count_stotinki_20 + count_stotinki_50 + count_levs_1 + count_levs_2))
