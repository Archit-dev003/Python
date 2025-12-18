import math

inp = int(input())
year = inp/365
year = math.floor(year)
print(year,"years")
month = ((inp-(365*year))/30)
month = math.floor(month)
print(month,"months")
day = (inp-((365*year)+(month*30)))
day = math.floor(day)
print(day,"days")   