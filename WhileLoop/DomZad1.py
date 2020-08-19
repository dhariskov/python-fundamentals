book_name = input()
book_count=int(input())

counter = 0
book_in_lybrary = ""
flag = False
while book_count > counter :

    book_in_lybrary=input()

    if book_in_lybrary==book_name:
        print(f"You checked {counter} books and found it.")
        flag = True
        break
    counter += 1

if not flag:
    print(f"The book you search is not here!")
    print(f"You checked {counter} books.")
