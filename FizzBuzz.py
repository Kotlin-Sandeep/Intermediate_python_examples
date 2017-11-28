l2=[]
def printFun(arg):    
    for num in arg:
        if num%3==0 and num%5==0:
            l2.replace(num,"FizzBuzz")
        elif num%3==0:
            l2.insert(num,"Fizz")
        elif num%5==0:
            l2.insert(num,"Fizz")
        else:
            print(num)

l1 = [i for i in range(100)]
printFun(list(l1))
print 'hello'
