# with문을 사용해서 with블록 내에서 자동으로 열고 닫음

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 공부\n")
    study_file.write("C언어 공부")

"""
study_file = open("study.txt", "w", encoding="utf8")
study_file.write("파이썬 공부\n")
study_file.write("C언어 공부")
study_file.close()
"""
# 같은 문장임
