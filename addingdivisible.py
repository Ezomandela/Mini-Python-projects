def solution(number):
    sum = 0
    if number < 0:
        return 0
    for i in range(1,number):
        sum = sum + i if i%3==0 or i%5==0 else sum
    return sum

print(solution(-1))