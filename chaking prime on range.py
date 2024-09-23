def solve (a,b):
    prime =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,97]
    count=0
    for number in range(a,b):
        if str(number)[-2:] == str(number**2)[-2:]:
              if int(str(number)[:2]) is prime and int(str(number**2)[:2]) is prime:
                 count+=1
    return count
print(solve(34,600))
