# 예제 1
print('###### Example_01 ######')
my_dict1 = {}
print(my_dict1)
print('')

# 예제 2
print('###### Example_02 ######')
my_dict2 = {1: 0, 1: -2, 2: 3.14}
print(my_dict2)
print('')

# 예제 3
print('###### Example_03 ######')
my_dict3 = {'name': 'alice', 'age': 10, 'vison': [1.0, 1.2]}
print(my_dict3)
print('')

# 예제 4
print('###### Example_04 ######')
clover = {'age': 27, 'job': 'soldier'}
print(clover)
clover['number'] = 1
print(clover)
print('')

# 예제 5
print('###### Example_05 ######')
clover = {'age': 27, 'job': 'soldier', 'number': 2}
print(clover['number'])
clover['number'] = 3
print(clover['number'])
print(clover.get('number'))
print('')

# 예제 6
print('###### Example_06 ######')
clover = {'age': 27, 'job': 'soldier', 'number': 2}
print(clover)
del clover['age']
print(clover)
print('')

# 예제 7
print('###### Example_07 ######')
order = {'spade': "bibim", 'diamon': 'hot'}
print(order)
order['clover'] = 'curry'
print(order)
order['diamon2'] = 'jjajang'
print(order)
del order['spade']
print(order)
print('')