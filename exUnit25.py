#딕셔너리에 키와 기본값 저장하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
print(x)
x.setdefault('f',100)
print(x)
x.update(a=90)
print(x)
x.update(e=50)
print(x)
x.update(a=900,f=60)
print(x)

y = {1: 'one', 2: 'two'}
y.update({1:'ONE', 3:'THREE'})
print(y)

y.update([[2,'TWO'],[4,'FOUR']])
print(y)

y.update(zip([1,2],['one','two']))
print(y)

#딕셔너리에서 키-값 쌍 삭제하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')
print(x)
print(x.pop('z',0))

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
del x['a']
print(x)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.popitem()
print(x)

#딕셔너리의 모든 키-값 쌍을 삭제하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear()
print(x)

#딕셔너리에서 키의 값을 가져오기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.get('a'))
print(x.get('z',0))

#딕셔너리에서 키-값 쌍을 모두 가져오기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.items())
print(x.keys())
print(x.values())

keys = ['a','b','c','d']
x = dict.fromkeys(keys)
print(x)
y = dict.fromkeys(keys, 100)
print(y)

from collections import defaultdict
y = defaultdict(int)
print(y['z'])

z = defaultdict(lambda: 'python')
print(z['a'])
