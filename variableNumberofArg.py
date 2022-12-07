# variable number of argument 

def average(*t):
    avg = sum(t)/len(t)
    print("average is :",avg)
average(4,5,6,7,8)
average(1,2,3,4,5,6,7,8,9)