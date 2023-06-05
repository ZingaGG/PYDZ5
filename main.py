# Task 1

# def AinB(a, b):
#     if b == 1:
#         return a
#     else:
#         a = a * AinB(a, b-1)
#         return a
    
# a, b = 2, 3
# print(AinB(a,b))

# Task 2

def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a+1, b-1)
        
    
a, b = 2, 5
print(f"Result = {sum(a,b)}")