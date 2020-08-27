score=int(input())
num=[90,80,70,60]
if score>=num[0]:
    result='A'
elif score>=num[1]:
    result='B'
elif score>=num[2]:
    result='C'
elif score>=num[3]:
    result='D'
else:
    result='F'
print(result)
