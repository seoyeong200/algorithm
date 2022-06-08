import sys
import os

print("os.getcwd() \n", os.getcwd()) # get current directory
print("os.chdir(path)\n" , os.chdir(os.getcwd())) # change directory to "path"
print("os.path.abspath(path)\n", os.path.abspath("directory")) # get "path"'s absolute directory
print(os.path.abspath("data-pipeline/notebooks/Untitled")) # 현재 디렉토리에 있는 파일 뿐만 아니라 로컬 전체 다 절대경로 뽑아줌

# 현재 파일의 절대경로
print(__file__)
# 절대경로에서 파일 이름 빼고 경로만 추출
print(os.path.dirname(__file__))



