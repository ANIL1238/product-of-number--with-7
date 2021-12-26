'''Objective
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a base-10 intege nr, , convert it to binary (base-2). Then find and print the base-10 integer denoting
the maximum number of consecutive 1
's in 's binary representation. When working with different bases, it is common to show the base as a subscript.'''
n = int(input().strip())
rmp = []
while n > 0:

    rp = n % 2
    n = n // 2
    rmp.append(rp)
    count, result = 0, 0
    for i in range(0, len(rmp)):
        if rmp[i] == 0:
            count = 0
        else:
            count += 1
print("the binary value of ",n ,"is",rmp)
print(max(result, count))
