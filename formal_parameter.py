def cheeseshop(kind, *args, **kwargs):
    print("-- Do you have any", kind,"?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in args:
        print(arg)
    print("-" *40)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])
        

cheeseshop("Limburger","It's very runny, sir",
           "It's really very, VERY runny, sir.",
           shopkeeper= "Sagar Nangare",
           Client="SevenMentor HR",
           sketch = "Cheese Shop Sketch")
