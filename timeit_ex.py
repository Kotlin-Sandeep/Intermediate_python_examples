import timeit

##input_list = range(100)
##def div_by_five(num):
##    if num % 5 ==0:
##        return True
##    else:
##        return False
##
##xyz = (i for u in input_list if div_by_five(i))
##
##xyz = [i for u in input_list if div_by_five(i)]

print(timeit.timeit('''
input_list = range(100)
def div_by_five(num):
    if num % 5 ==0:
        return True
    else:
        return False

xyz = (i for u in input_list if div_by_five(5000))
'''))
