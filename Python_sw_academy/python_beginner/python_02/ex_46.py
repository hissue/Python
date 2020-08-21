'''
name 프로퍼티를 가진 Student를 부모 클래스로 major 프로퍼티를 가진
GraduateStudent 자식 클래스를 정의하고 이 클래스의 객체를
다음과 같이 문자열로 출력하는 코드를 작성하십시오.

출력
이름: 홍길동
이름: 이순신, 전공: 컴퓨터
'''

class Student:
    names='이름'
    majors='전공'

    @property
    def name(self):
        return '이름: {}'.format(self.names)

class GraduateStudent(Student):
    def __init__(self,name,major):
        self.names = name
        self.majors=major

    @property
    def major(self):
        return '전공: {}'.format(self.majors)
    def p_major(self):
        return


b=GraduateStudent('홍길동','')
print('{}'.format(b.name))
b=GraduateStudent('이순신','컴퓨터')
print('{}, {}'.format(b.name,b.major))
