year=int(input())
if year%4==0:
    if not year%100==0 or year%400==0:
        result=1
    else:
        result=0
else:
    result=0

print(result)
