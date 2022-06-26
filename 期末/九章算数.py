a = int(input())
day = 1
big = 1
totalbig = 1
small = 1
totalsmall = 1
while True:
    day += 1
    big = big * 2
    totalbig += big
    small = small * 0.5
    totalsmall += small
    if totalbig + totalsmall >= a:
        break

print(day)
