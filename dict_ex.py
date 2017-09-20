#a= [1,10,20,47,74,63,59,99,106,120,133,155,174,162,188,199,200,210,222]
def bin_search(a,key):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = low + ((high-low)/2)
        if a[mid] == key:
            return mid
        elif key<a[mid]:
            high = mid-1
        else:
            low = mid+1
            return -1

b= [1,10,20,47,74,63,59,99,106,120,133,155,174,162,188,199,200,210,222]
bin_search(b, 47)
    
