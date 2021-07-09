total = 0
for x in range(0, 1000):
    if (x/3).is_integer() or (x/5).is_integer():
        print(x)
        total = total + x
print(total)

