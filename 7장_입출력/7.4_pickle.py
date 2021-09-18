# 프로그램상에서 사용하고 있는 데이터를 파일 형태로 저장해주는 것
import pickle
### 입력 ###
profile_file = open("profile.pickle", "wb")
# profile.pickle 파일을 이진쓰기모드(wb)로 생성후 열기
# pickle파일은 무조건 바이너리형태 모드를 사용해야함
profile = {"이름": "김씨", "나이": 30, "취미": ["축구", "골프", "배구"]}
pickle.dump(profile, profile_file)
# profile에 있는 정보를 profile_file에 저장
profile_file.close()

### 출력 ###
profile_file = open("profile.pickle", "rb")
# 이진읽기모드(rb)로 파일을 읽어옴
profile = pickle.load(profile_file)
# profile_file파일에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
