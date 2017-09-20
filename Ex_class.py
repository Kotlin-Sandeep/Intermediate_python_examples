class MyClass:
    number = 0
    name = "noname"
def Main():
    me = MyClass()
    me.number = 1337
    me.name = "Sagar"

    friend = MyClass()
    friend.number = 5
    friend.name = "Akash"

    empty = MyClass()

    print("Name: " + me.name +", Favorite Number: "+ str(me.number))
    print("Name: " + friend.name +", Favorite Number: "+ str(friend.number))
    print("Name: " + empty.name +", Favorite Number: "+ str(empty.number))
if __name__=="__main__":
    Main()
