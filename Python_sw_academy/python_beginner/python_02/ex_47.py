'''
반지름 정보를 갖고, 원의 면적을 계산하는 메서드를 갖는 Circle 클래스를 정의하고,
생성한 객체의 원의 면적을 출력하는 프로그램을 작성하십시오.

출력
원의 면적: 12.56
'''
class Circle:
    def __init__(self,value):
        self.values=value
        self.ca=0

    def mun_cal(self):
        self.ca=pow(self.values,2)*3.14
        return self.ca


result=Circle(2)
print('원의 면적: {:0.2f}'.format(result.mun_cal()))

