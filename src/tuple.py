# 예제 1
print('###### Example_01 ######')
clovers = ('clover', 'hart1', 'hart2')
print(clovers)
# clovers[0] = 'clover1' # 튜플의 값을 변경하려고 하면 에러 발생
print('')

# 예제 2
print('###### Example_02 ######')
my_int = (1)
print(type(my_int))
my_tuple = (1,)
print(type(my_tuple))
print('')

# 예제 3
print('###### Example_03 ######')
clovers = 'clover', 'clover2', 'clover3' # 패킹
print(clovers)
alice_blue = (240, 248, 255)
r, g, b = alice_blue # 언패킹
print('R:', r, 'G:', g, 'B:', b)
print('')

# 예제 4
print('###### Example_04 ######')
dodo = 'mint'
alice = 'strawberry'
print('dodo:', dodo, ", alice:", alice)
dodo, alice = alice, dodo # 패킹 & 언패킹 동시에
print('dodo:', dodo, ", alice:", alice)
print('')
