def generator_function():
    for i in range(11):
        yield i
l1=[]
l2=[]
for item in generator_function():
    if item%2==0:
        l1.append(item)
        print(item,': even')
    elif item%3==0:
        l2.append(item)
        print(item,': odd')
print("Even List is: ",l1)
print("Odd List is: ",l2)
    
