set_1 = {10, 20, 20, 30}
set_2 = {30, 30, 40, 50}

### 세트 메소드 ###

# 교집합(intersection())
print(set_1.intersection(set_2))  # {30}

# 합집합(union())
print(set_1.union(set_2))  # {50, 20, 40, 10, 30}

# 차집합(difference())
print(set_1.difference(set_2))  # {10, 20}
print(set_2.difference(set_1))  # {40, 50}

# 여집합(symmetric_difference())
print(set_1.symmetric_difference(set_2))  # {40, 10, 50, 20}

set = {10, 20, 30, 40}

# 요소 추가: add()
set.add(50)
print(set)  # {40, 10, 50, 20, 30}

# 여러 요소추가: update()
set.update([60, 70])
print(set)  # {70, 40, 10, 50, 20, 60, 30}

# 요소 제거: remove()
set.remove(60)
print(set)  # {70, 40, 10, 50, 20, 30}

# 요소 제거: discard()
set.discard(70)
print(set)  # {40, 10, 50, 20, 30}

# 모든요소제거: clear()
set.clear()
print(set)  # set()
