film_type = input()
rows = int(input())
columns = int(input())

if film_type=="Premiere" :
    print(f"{rows*columns*12:.2f} leva")
elif film_type=="Normal" :
    print(f"{rows * columns * 7.5:.2f} leva")
else:
    print(f"{rows * columns * 5:.2f} leva")

