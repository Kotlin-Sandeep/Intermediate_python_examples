class Singleton(type):
    _instances = {}
    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singletn,cls).__call__(*args,**kwargs)
            cls.x = 5
        return cls._instances[cls]
class MyClass(object):
    __metaclass__ = Singleton

m = MyClass()
v = MyClass()

print(m.x)
m.x = 9
print(v.x)
            
