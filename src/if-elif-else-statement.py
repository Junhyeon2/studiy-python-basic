
# 예제 1
print('###### Example_01 ######')
if True:
    print('is True')
print('')

# 예제 2
print('###### Example_02 ######')
if False:
    print('is False')
print('')

# 예제 3
print('###### Example_03 ######')
socre = 90
if socre > 80:
    print("pass")
print('')

# 예제 4
print('###### Example_04 ######')
socre = 60
if socre > 80:
    print('pass')
else:
    print('fail')
print('')

# 예제 5
print('###### Example_05 ######')
socre = 30
if socre > 80:
    print('A')
elif 60 < socre <= 80:
    print('B')
elif 40 < socre <= 60:
    print('C')
else:
    print('F')
print('')

# 예제 6
print('###### Example_06 ######')
fee = 0
ages = [10, 20, 21, 40, 32, 30, 15, 6]

for age in ages:
    if age >= 20:
        fee += 1000;
    elif age >= 8:
        fee += 500
    else:
        fee += 100
print(fee)
print('')

# 예제 7
print('###### Example_07 ######')
games = 12
point = 25
if games >= 12 and point >= 20:
    print('MVP')
print('')