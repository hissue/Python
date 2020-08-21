'''
국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고
메서드를 호출하는 코드를 작성해봅시다.
출력
대한민국
대한민국
'''
class Korean:

    @staticmethod #인스턴스를 통하지 않고 클래스에서 바로 호출할 수 있는 정적 메서드와 클래스 메서드
    def printNati1onality(other):
        print(other)
# nation=Korean('대한민국')
for i in range(2):
    Korean.printNati1onality('대한민국')
