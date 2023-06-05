# Task 1

def AinB(a, b):
    if b == 1:
        return a
    else:
        a = a * AinB(a, b-1)
        return a
    
a, b = 2, 3
print(AinB(a,b))