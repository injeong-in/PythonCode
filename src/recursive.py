

def sum(integer, count, sum_value):
    if integer >= count:
        return
    integer += 1
    sum_value += integer

    sum(integer, count, sum_value)




# def exam(integer):
#     if integer > 10:
#         return integer
#     else:
#         return '오류입니다'
#
# value = exam(20)
# print(value)

sum(0,10,0)