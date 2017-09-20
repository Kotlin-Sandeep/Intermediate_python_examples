##def fibon(n):
##    a=b=1
##    for i in range(n):
##        yield a
##        a,b = b,a+b
##
##for x in fibon(10):
##    print("Fibonnaci sequence of "+ str(x) + " element is: "+str(x))

#Another Way of doing so

def fibon(n):
    a=b=1
    res = []
    for i in range(n):
        res.append(a)
        a,b = b, a+b
    return res

for x in fibon(10):
    print(x)
