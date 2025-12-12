import math
A,B=input().split()
A=int(A)
B=int(B)
print("floor",A,"/", B, "=",math.floor(A/B))
print("ceil",A,"/", B, "=",math.ceil(A/B))
print("round",A,"/", B, "=",math.floor((A/B)+0.5))
