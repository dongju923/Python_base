fruit = {"사과", "망고", "수박"}
print(fruit, type(fruit))
# {'망고', '수박', '사과'} <class 'set'>

fruit = list(fruit)
print(fruit, type(fruit))
# ['사과', '수박', '망고'] <class 'list'>

fruit = tuple(fruit)
print(fruit, type(fruit))
# ('사과', '망고', '수박') <class 'tuple'>

fruit = set(fruit)
print(fruit, type(fruit))
# {'사과', '수박', '망고'} <class 'set'>
