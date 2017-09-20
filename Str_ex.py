import os
fname = 'DataSet.txt'
print('\\'+fname)

with open(os.path.join(fname)) as f:
    print(f.read())
