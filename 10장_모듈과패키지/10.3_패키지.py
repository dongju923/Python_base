# 하나의 디렉토리에 모듈들을 모아놓은 집합

from travel import vietnam
import travel.thailand
# travel패키지의 thailand모듈 import
# import를 사용할때 뒷부분은 모듈이나 패키지만 작성가능(클래스나 함수는 작성불가)
from travel.thailand import ThailandPackage
# from을 사용하면 import뒤에 클래스나 함수까지 작성 가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
# [태국패키지 3박 5일] 방콕, 파타야 여행 50만원

trip_to = vietnam.VietnamPackage()
trip_to.detail()
# [베트남패키지 3박 5일] 다낭, 호도 여행 60만원
