

def sum(integer, count, sum_value = 0):
    #param: integer = 시작값, count = 마지막 값
    if integer > count:
        return sum_value
    else:
        sum_value += integer
        integer += 1
        return sum(integer, count, sum_value)



value = sum(1,100)
print('최종값: ', value)