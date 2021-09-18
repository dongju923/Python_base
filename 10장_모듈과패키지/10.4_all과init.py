from travel import *
# 패키지로부터 import *을 하면 오류가 남
# 실제로는 사용자가 공개범위를 설정해줘야함
# __init__.py 에서 __all__메서드로 설정 가능

trip_to = vietnam.VietnamPackage()
trip_to.detail()
# [베트남패키지 3박 5일] 다낭, 호도 여행 60만원


trip_to = thailand.ThailandPackage()
trip_to.detail()
# [태국패키지 3박 5일] 방콕, 파타야 여행 50만원
