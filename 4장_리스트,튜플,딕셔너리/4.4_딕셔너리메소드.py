dic = {"Number1": "One", "Number2": "Two", "Number3": "Three"}

### 키 값 가져오기 ###
print(dic.keys())  # dict_keys(['Number1', 'Number2', 'Number3'])

### 벨류 값 가져오기 ###
print(dic.values())  # dict_values(['One', 'Two', 'Three'])

### 키:벨류 쌍으로 가져오기 ###
print(dic.items())
#dict_items([('Number1', 'One'), ('Number2', 'Two'), ('Number3', 'Three')])

### 키에 해당하는 값 가져오기 ###
print(dic.get("Number2"))  # Two

### 해당 키값 빼기 ###
dic.pop("Number3")
print(dic)  # {'Number1': 'One', 'Number2': 'Two'}

### 모두 초기화 ###
dic.clear()
print(dic)  # {}
