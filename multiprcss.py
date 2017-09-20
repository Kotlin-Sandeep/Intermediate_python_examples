import multiprocessing

def spawn(num1, num2):
    print('Spawned! {} {}'.format(num1, num2))

if __name__=='__main__':
    for i in range(100):
        P = multiprocessing.Process(target=spawn,args=(i,i+1))
        P.start()
        P.join()

