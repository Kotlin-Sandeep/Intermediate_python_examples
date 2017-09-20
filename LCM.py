def gcd(x,y):
    while(y):
        x,y=y, x%y
    return x
def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if ((greater%x==0) and (greater%y==0)):
            lcm = greater
            break
        greater +=1
    return lcm
num1 = int(raw_input("Please enter first Element:"))
num2 = int(raw_input("Please enter Second Element:"))

print("The L.C.M of ", num1," and ", num2, " is ", lcm(num1,num2))
print("The G.C.D of ", num1," and ", num2, " is ", gcd(num1,num2))
