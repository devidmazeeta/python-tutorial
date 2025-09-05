# break => Terminates loop
# continue => Jumps to next loop

num = 100
while num > 0:
    num -= 1
    if num % 5 == 0:
        if num == 20:
            break
        continue
    print(num)
else:
    print("while loop ended")

for n in range(100):
    for i in range(n):
        if n == 5:
            break
        print(i)

    if n == 5:
        break
else:
    print("For loop ended")
