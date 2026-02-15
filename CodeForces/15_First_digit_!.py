import math
inp = int(input())

if(inp>=100 and inp<=999): 
    num = inp/100
    num = math.floor(num)
    if(num%2==0):
        print("EVEN")
    elif(num%2!=0):
        print("ODD") 