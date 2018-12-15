# for loop 사용 예제

# 여제 1
for num in range(10):
    print('num is ', num)

# 여제 2
for num in range(1, 10):
    print('2 *', num, '=' ,2 * num)

# 예제 3
for num in [0, 1, 2]:
    print(num)

# 예제 4
characters = ['alice', 'bird', 'rabbit']
for character in characters:
    print(character)

# 에제 5
players = ['queen', 'rabbit', 'hart', 'hat']
for player in players:
    print(player, '!!')
    print(players) # 들여쓰면, for 문 안에 있는 것으로 간주.
print(players)

# 에제 6
introduce = 'hello my name is junhyeon'
for char in introduce:
    print(char)

# 예제 7
roses = ['white', 'white', 'white']
for i in range(3):
    roses[i] = 'red'
print(roses)