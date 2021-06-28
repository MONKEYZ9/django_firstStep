# keyword Arguments
# 키워드 기반으로 넘겨줄 때 이렇게 된다고 보면 된다.

# 위치기반과 키워드 기반으로 메소드를 구성할 수 있다.
# Positional Arguments vs keyword Arguments

# Optional Data 평소에 사용하지 않지만 가끔 사용할때는 어떻게 하냐
# 함수에 선언되어있는데 입력에 넣지 않으면 에러가 뜸
# TypeError가 뜨게 된다.

# 근데 우리는 선택적으로 데이터를 넣고 싶은데
# 그걸 해결해주는게
# *args
# def test(name, age, *args) :
#  => 이런식으로 하면 선택적으로 할 수 있따는 거야
#  test(name, age, '선택적 인자')
#  print(*args) ==> 선택적 인자
#  print(type(*args)) ==> 튜플이다.

# **kwargs = >keyword Arguments + Optional Data
# 키워드 기반으로 한 것을 자유롭게 받을 수 있게 된다.
# def test(name, age, **kwargs) :
#  => 이런식으로 하면 선택적으로 할 수 있따는 거야

# test(name, age, xxx = '선택적 인자')


# print(*args) ==> 선택적 인자
#  print(type(*args)) ==> 딕셔너리이다. => {xxx : '선택적 인자'}

# def test3(*arg, **kwarg):
    # => 이걸 보더라도 쫄지말고
    # 위치기반과 키워드기반의 Optinal Data를 기억해놓고 있으면 된다

# class
# 무엇이 프로그래밍인지 프로그래밍을 어떻게 하는지를 알 수 있다는 거야
# 문제를 해결하기 위해서 그 처리바법과 순서를 기술하는 것이다
# PP와 OOP
# 절차지향과 객체지향으로 나눠지게 된다.
# 객체 변수 메서드를 이해해야 한다.
# 객체란? ->
# 객체를 알기 위해서는 객체 인스턴스 => 클래스를 알아야 한다.
#
# class Car:
#     pass
# santafe = Car()
# santafe는 객체 되고
# class Car는 클래스
#
# 필요한 속성
# class Car:
#     def __init__(self):
#         메소드 안에는 self라는 걸 넣어야 해 객체 자신을 의미하는 것
# init을 정리할 필요가 있어 보인다.

# Class 실습을 할 수 있다.
# 프로그램 순서와 자료구조를 분리해야한다
#
# Super Method를 어떻게 사용해야 할까? => 부모 클래스 메소드를 재사용하는거야
# class Fruit(Items):
#     def __init__(self, *args):
#         super().__init__(self)


# 인스턴스
# 판단해주는 메소드다.

# 선택적 인자를 넘겨줄 수 도 있고 안할 수도 있다

# 절차지향은 순서를 먼저 생각하고
# 객체지향은 사물 혹은 물체의 기능들을 먼저 설계하고 생각한다
# 상속에 기반한 코드 재사용성을 향상 시키는 것이 super()라고 한다