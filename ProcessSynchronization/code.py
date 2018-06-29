# -*- coding: utf-8 -*-

import _thread
import queue
N = 16
mutex = 0
full = 0
empty = 0
buffer = queue.Queue()

#wait(S)原子操作
def wait(S):
    while S<=0:
        pass
    
    S = S -1

#signal(S)原子操作
def signal(S):
    S = S + 1

#写者线程操作函数
def writerProcessing():
    while 1:
        x = int(input("写入数据（写者进程）："))
        wait(empty)
        buffer.put(x)
        signal(full)
        if x == 999:
            break

#读者线程操作函数
def readerProcessing():
    while 1:
        wait(full)
        x = buffer.get()
        signal(empty)
        print("读取数据(读者线程)："+str(x))
        if x == 999:
            break
        

# 创建两个线程
try:
   _thread.start_new_thread(writerProcessing)
   _thread.start_new_thread(readerProcessing)
except:
   print ("Error: 无法启动线程")

while 1:
   pass