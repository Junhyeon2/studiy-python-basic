# 내장 함수: python에 포함된 함수
# - print(), range(), ...
# 모듈의 함수: 비슷한 함수 끼리 모아놓은 집합
# 사용자 정의 함수

# 예제 1
print('###### Example_01 ######')
def my_func():
    print("hello python fuction")
my_func()
print()

# 예제 2
print('###### Example_02 ######')
def add(num1, num2):
    return num1 + num2
print(add(2, 3))
print()

# 예제 3
print('###### Example_03 ######')
def add_mul(num1, num2):
    return num1 + num2, num1 * num2
print(add_mul(3,4))
print()

# 예제 4
print('###### Example_04 ######')
def judge_cards(name):
    print(name, '1 guiltiness!')
    print(name, '2 guiltiness!')
    print(name, '3 guiltiness!')

judge_cards('hart')
judge_cards('clover')
judge_cards('spade')
print()