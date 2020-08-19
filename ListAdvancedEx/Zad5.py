electrons = int(input())
atom=[]
level=1
counter_electrons = 0

while electrons-counter_electrons>2*level**2:
    counter_electrons += 2*level**2
    atom.append(2*level**2)
    level += 1

if electrons-counter_electrons!=0:
    atom.append(electrons - counter_electrons)
print(atom)