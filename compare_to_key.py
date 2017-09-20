def cmp_to_key(mycmp):
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj)<0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj)>0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj)==0

        def __le__(self, other):
            return mycmp(self.obj, other.obj)<=0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj)>=0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj)!=0
    return K

sorted([5,2,4,1,3], key = cmp_to_key(reverse_numeric)) 
        
        
        
        
