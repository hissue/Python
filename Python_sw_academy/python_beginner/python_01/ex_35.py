'''
사용자 2명으로부터 가위, 바위, 보를 입력 받아
가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.
입력
홍길동
이순신
가위
바위

출력
바위가 이겼습니다!
'''
def ch_rsp(man1,man2):
    rsp=[['가위','보'],['보','바위'],['바위','가위']]
    for i in range(len(rsp)):
        if man1 in rsp[i] and man2 in rsp[i]:
            if man1 == rsp[i]:
                re= man1
            else:
                re= man2
    return re

man1_name=input()
man2_name=input()
man1_rsp=input()
man2_rsp=input()
#man1=[man1_name,man1_rsp]
#man2=[man2_name,man2_rsp]
result_value=ch_rsp(man1_rsp,man2_rsp)
print('%s가 이겼습니다!'%result_value)

