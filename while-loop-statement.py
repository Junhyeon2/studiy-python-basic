# 예제 1
print('###### Example_01 ######')
num = 0
while num < 3:
    print('hello while', num)
    num += 1
print('')

# 에제 2
print('###### Example_02 ######')
answer = ''
while answer != 'Seoul':
     answer = input('Where is the capital of Korea?')
print('The answer is correct.')
print('')

# 예제 3
print('###### Example_03 ######')
count = 0
while count < 3:
    count = count + 1
    if count == 2:
        continue
    print(count)
print('')

# 예제 4
print('###### Example_04 ######')
count = 0
while count < 3:
    count = count + 1
    if count == 2:
        break
    print(count)
print('')

# 예제 5
print('###### Example_05 ######')
while True:
    answer = input('In Seoul, Madrid and London, where is the capital city of Korea?')
    if answer == 'Seoul':
        print('The answer is correct.')
        break
    elif answer == 'Madrid':
        print('Madrid is the capital of Spain.')
    elif answer == 'London':
        print('London is the capital of England.')
    else:
        print('Please pick it again.')
print('')