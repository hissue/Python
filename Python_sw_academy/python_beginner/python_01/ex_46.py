'''
"ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와

같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된

알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.

출력
184
'''
def calcurate(l,n):
    while 'F' in l:
        l.remove('F')
    n.append(l)
    return n

eng="ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
a_str=list(map(lambda a: ord('A')*4 if a=='A' else 'F', eng))
b_str=list(map(lambda b: ord('B')*3 if b=='B' else 'F', eng))
c_str=list(map(lambda c: ord('C')*2 if c=='C' else 'F', eng))
d_str=list(map(lambda d: ord('D')*1 if d=='D' else 'F', eng))
temp=[a_str,b_str,c_str,d_str]
new=[]
tot=[]
for i in temp:
    tot=list(calcurate(i,new))

tot[0]=sum(tot[0])/ord('A')
tot[1]=sum(tot[1])/ord('B')
tot[2]=sum(tot[2])/ord('C')
tot[3]=sum(tot[3])/ord('D')
print(int(sum(tot)))

# a=list(map(lambda a: int(a/ord('A')) if a!=2 else 2,a_str))
# b=list(map(lambda b: int(b/ord('B')) if b!=2 else 2,b_str))
# c=list(map(lambda c: int(c/ord('C')) if c!=2 else 2,c_str))
# d=list(map(lambda c: int(c/ord('C')) if c!=2 else 2,c_str))
# a.remove(2)
# b.remove(2)
# c.remove(2)

#
# print(tot)
# for i in range(len(tot)):
#     k.append(int(tot[i]/ord(a[i]))
# #print(sum(k))




