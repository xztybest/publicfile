import subprocess  
#import re
def pingx(yf):
    p = subprocess.Popen(["ping.exe", yf],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
    shell = True)  
##out = p.stdout.read()  
    print ('Result:---- \n')
##    print ("成功")


y=input("请输入次数\n")
yf=input("请输入网址\n")

for i in range(int(y)):
    pingx(yf)
##p = subprocess.Popen(["ping.exe", 'www.baidu.com'],
##  stdin = subprocess.PIPE,
##  stdout = subprocess.PIPE,
##  stderr = subprocess.PIPE,
##  shell = True)  
####out = p.stdout.read()  
##print ('Result:---- \n')
##print ("成功")
