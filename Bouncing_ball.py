h = int(input("Enter Height: "))
b = int(input("Enter Number of Bounces: "))
bounces1 = 0
bounces2 = 0

d = h*0.5
for eachpass in range(b):
    if eachpass ==1:
        bounces1 = h + d
    if eachpass == 2:
        bounces2 = bounces1 + h + d

print(str(bounces2))
