class ThailandPackage():
    def detail(self):
        print("[태국패키지 3박 5일] 방콕, 파타야 여행 50만원")


# __main__
# 패키지 자체를 실행하기 위한 용도
# 패키지를 실행시키면 __main__동작
if __name__ == "__main__":
    print("이 문장은 모듈을 직접 실행할때 작동")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("외부에서 모듈 호출")
