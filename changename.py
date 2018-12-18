import os

os.chdir(r'C:\Users\student\change\SSAFY지원자')

for filename in os.listdir("."):
    data = filename.replace('SAMSUNG','SSAFY')
    os.rename(filename,data)
    #os.rename(filename,"SAMSUNG"+filename)

#split를 이용하여 처리하기
##filename.split(내용)

##심화 이외의 방도