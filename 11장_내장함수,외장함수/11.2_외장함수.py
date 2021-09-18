# 내장함수와는 다르게 import 해서 사용이 가능
# 외장함수 목록 -> # 내장함수 목록 -> https://docs.python.org/3/py-modindex.html


import os
# os : 운영체제에서 제공하는 기본 기능
import glob
# glob : 경로내의 폴더 / 파일 목록 조회


print(glob.glob("*.py"))
# 확장자가 .py인 모든 파일
print(os.getcwd())
# 현재 디렉토리 출력
print(os.listdir())
# 현재 경로에 모든 폴더를 출력

folder = "sample_dir"

if os.path.exists(folder):  # 현재 경로에 folder가 존재하는지 체크
    print("이미 존재하는 폴더입니다. ")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)  # 폴더가 없으면 새로 생성
    print(folder, "폴더를 생성하였습니다")
