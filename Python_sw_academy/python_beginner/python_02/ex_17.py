'''
단어를 콤마(,)로 구분해 입력하면 그 단어들을 사전순으로 정렬해 출력하는 프로그램을 작성하시시오.

입력
python, hello, world, hi

출력
hello, hi, python, world
'''

a= input().split(', ')
a.sort()
result=""
for i in a:
    result+='%s, '%i
print(result[0:-2])