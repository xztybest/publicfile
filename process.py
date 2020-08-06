from multiprocessing import Process
import time
import os
##多线程启动应用
def CCOPEN(name):
    os.startfile("D:\\NSUCC\\NSUCC.exe")
def QQopen(name):
    os.startfile("D:\QQ\Bin\QQScLauncher.exe")
def Browseropen(name):
    os.startfile("D:\google\Google3\App\chrome.exe")
if __name__=='__main__':
    p1=Process(target=CCOPEN,args=('CCopen',))
    p2=Process(target=QQopen,args=('QQopen',))
    p3=Process(target=Browseropen,args=('Chromopen',))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
    p1.terminate()
    p2.terminate()
    p3.terminate()
    print(end)

    
       
