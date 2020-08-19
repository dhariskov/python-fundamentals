lenght = int(input())
width = int(input())

cake = lenght * width
pieces_taken_counter = 0

while pieces_taken_counter < cake:
    pieces_taken = input()
    if pieces_taken == "STOP":
        print(f"{cake - pieces_taken_counter} pieces are left.")
        break

    pieces_taken_counter = pieces_taken_counter + int(pieces_taken)

if pieces_taken_counter >= cake:
    print(f"No more cake left! You need {pieces_taken_counter - cake} pieces more.")
