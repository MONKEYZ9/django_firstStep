# keyword Arguments
# 키워드 기반으로 넘겨줄 때 이렇게 된다고 보면 된다.

# 위치기반과 키워드 기반으로 메소드를 구성할 수 있다.
# Positional Arguments vs keyword Arguments

# Optional Data 평소에 사용하지 않지만 가끔 사용할때는 어떻게 하냐
# 함수에 선언되어있는데 입력에 넣지 않으면 에러가 뜸
# TypeError가 뜨게 된다.

# 근데 우리는 선a택적으로 데이터를 넣고 싶은데
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