#딕셔너리 사용하기
lux = [490,334,5500,18.72]
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux)

#키 이름이 중복되면?
lux = {'health': 490, 'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux['health'])
print(lux)

#딕셔너리 키의 자료형
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
print(x)

#빈 딕셔너리 만들기
x = {}
y = dict()
print(x,y)

lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
print(lux1)
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
print(lux2)
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
print(lux3)
lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
print(lux4)

#딕셔너리의 키에 접근하고 값 할당하기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux['health'])
print(lux['mana'])

#딕셔너리의 키에 값 할당하기
lux['health'] = 2037
lux['mana'] = 1184
print(lux)
print('health' in lux)
print('attack_speed' in lux)
print('attack_speed' not in lux)
print('health' not in lux)
lux['aaa'] = 123
print(lux)
print(len(lux))
