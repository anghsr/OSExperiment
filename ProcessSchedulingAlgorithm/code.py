# -*- coding: utf-8 -*-
import numpy as np

#定义变量
ArrivalTime = []
ServiceTime = []
FinishTime = []
WholeTime = []
WeightWholeTime = []
AverageWT_FCFS = float(0.0)
AverageWT_SJF = float(0.0)
AverageWWT_FCFS = float(0.0)
AverageWWT_SJF = float(0.0)


#各个变量的输入
#输入n
n = int(input("输入进程个数n："))
#输入Tn
tmp = 0
print("输入到达时间：")
while tmp<n:
    num = tmp+1
    x = input("进程"+chr(num+64)+"的到达时间：")
    ArrivalTime.append(int(x))
    tmp = tmp + 1
#输入Sn
tmp = 0
print("输入服务时间：")
while tmp<n:
    num = tmp+1
    x = input("进程"+chr(num+64)+"的服务时间：")
    ServiceTime.append(int(x))
    tmp = tmp + 1
#选择算法
Algorithms = int(input("选择算法（1=FCFS,2-SJF）："))

def FCFS():
    '''
        先来先服务（first-com first-served,FCFS)调度算法
    '''
    #到达序列
    #创建一个临时可以修改的的列表ArTmp来表示到达时间，解决到达时间相同的问题
    ArrivalT = ArrivalTime[:]
    ArTmp = ArrivalTime[:]
    ArrivalT.sort()
    ArrivalList = []
    for x in ArrivalT:
         ArrivalList.append(ArTmp.index(x))
         ArTmp[ArTmp.index(x)] = None 


    #完成时间
    time = ArrivalTime[ArrivalList[0]]  #第一个作业到达时间
    FinishTime = [0 for x in range(0,n)]
    for x in ArrivalList:
        print("时刻"+str(time)+"：进程"+chr(x+65)+"开始运行")
        FinishTime[x] = time + ServiceTime[x]
        time = FinishTime[x]

    #周转时间
    WholeTime = [0 for x in range(0,n)]
    tmp = np.array(WholeTime)
    A = np.array(ArrivalTime)
    F = np.array(FinishTime)
    tmp = F - A
    WholeTime = tmp.tolist()

    #带权周转时间
    WeightWholeTime = [float(0.0) for x in range(0,n)]
    tmp = np.array(WholeTime)
    S = np.array(ServiceTime)
    Wtmp = np.array(WeightWholeTime)
    Wtmp = tmp/S
    x = int(Wtmp.shape[0])-1
    while x>-1:
        Wtmp[x] = float('%0.2f' % Wtmp[x])
        x = x - 1
    WeightWholeTime = Wtmp.tolist()

    #平均周转时间
    sum = float(0.0)
    for x in WholeTime:
        sum = sum + x
    AverageWT_FCFS = round(sum/n,2)
    
    #平均带权周转时间
    sum = float(0.0)
    for x in WeightWholeTime:
        sum = sum + x
    AverageWWT_FCFS = round(sum/n,2)
    
    print('---------------------------------------------------------------')
    print('进程名',end='           ')
    i = 0
    while i<n:
        print(chr(i+65),end='       ')
        i = i + 1
    print("  平均")
    print('到达时间',end='         ')
    for i in ArrivalTime:
        print(i,end='       ')
    print()
    print('服务时间',end='         ')
    for i in ServiceTime:
        print(i,end='       ')
    print()
    print('---------------------------------------------------------------')
    print('完成时间',end='         ')
    for i in FinishTime:
        print(i,end='       ')
    print()
    print('周转时间',end='         ')
    for i in WholeTime:
        print(i,end='       ')
    print(AverageWT_FCFS)
    print("带权周转时间",end='    ')
    for i in WeightWholeTime:
        print(i,end='     ')
    print(AverageWWT_FCFS)
    print('---------------------------------------------------------------')

def SJF():
    '''
        短作业优先(short job first,SJF)的调度算法
    '''
    #到达序列
    #创建一个临时可以修改的的列表ArTmp来表示到达时间，解决到达时间相同的问题
    ArrivalT = ArrivalTime[:]
    ArTmp = ArrivalTime[:]
    ArrivalT.sort()
    ArrivalList = []
    for x in ArrivalT:
         ArrivalList.append(ArTmp.index(x))
         ArTmp[ArTmp.index(x)] = None 
    
    
    #完成时间
    minNo = 0
    FinishTime = [0 for x in range(0,n)]
    z = ArrivalTime[ArrivalList[0]] #获取第一个到达的时间
    ArrivalT = ArrivalTime[:]
    num = ArrivalTime.count(z)  #判断最先到达的作业是否只有一个
    if num == 1:
        pass
    else:
        tmp = []
        for x in ArrivalT:
            if z == x:
                tmp.append(ArrivalT.index(x))
        tmpServiceTime = []
        for x in tmp:
            tmpServiceTime.append(ServiceTime[x])
        tmpServiceTime.sort()
        minNo = ServiceTime.index(tmpServiceTime[0])
        z = ArrivalTime[minNo]
    FinishTime[minNo] = z + ServiceTime[minNo]
    ArrivalT.remove(ArrivalT[minNo])    #去掉已运行的第一个作业
    time = FinishTime[minNo]
    print("时刻"+str(time-ServiceTime[minNo])+"：进程"+chr(minNo+65)+"开始运行")
    No = n -1
    while No>0:
        already = []
        for a in ArrivalT:
            if a<=time:
                already.append(ArrivalTime.index(a))
        alreadyWorkServiceTime = []
        for a in already:
            alreadyWorkServiceTime.append(ServiceTime[a])
        alreadyWorkServiceTime.sort()
        minNo = ServiceTime.index(alreadyWorkServiceTime[0])
        FinishTime[minNo] = time + ServiceTime[minNo]
        ArrivalT.remove(ArrivalTime[minNo])    #去掉已运行的作业
        time = FinishTime[minNo]
        No = No - 1
        print("时刻"+str(time-ServiceTime[minNo])+"：进程"+chr(minNo+65)+"开始运行")
   
    #周转时间
    WholeTime = [0 for x in range(0,n)]
    tmp = np.array(WholeTime)
    A = np.array(ArrivalTime)
    F = np.array(FinishTime)
    tmp = F - A
    WholeTime = tmp.tolist()

    #带权周转时间
    WeightWholeTime = [float(0.0) for x in range(0,n)]
    tmp = np.array(WholeTime)
    S = np.array(ServiceTime)
    Wtmp = np.array(WeightWholeTime)
    Wtmp = tmp/S
    x = int(Wtmp.shape[0])-1
    while x>-1:
        Wtmp[x] = float('%0.2f' % Wtmp[x])
        x = x - 1
    WeightWholeTime = Wtmp.tolist()

    #平均周转时间
    sum = float(0.0)
    for x in WholeTime:
        sum = sum + x
    AverageWT_SJF = round(sum/n,2)
    
    #平均带权周转时间
    sum = float(0.0)
    for x in WeightWholeTime:
        sum = sum + x
    AverageWWT_SJF = round(sum/n,2)
    
    print('---------------------------------------------------------------')
    print('进程名',end='           ')
    i = 0
    while i<n:
        print(chr(i+65),end='       ')
        i = i + 1
    print("  平均")
    print('到达时间',end='         ')
    for i in ArrivalTime:
        print(i,end='       ')
    print()
    print('服务时间',end='         ')
    for i in ServiceTime:
        print(i,end='       ')
    print()
    print('---------------------------------------------------------------')
    print('完成时间',end='         ')
    for i in FinishTime:
        print(i,end='       ')
    print()
    print('周转时间',end='         ')
    for i in WholeTime:
        print(i,end='       ')
    print(AverageWT_SJF)
    print("带权周转时间",end='    ')
    for i in WeightWholeTime:
        print(i,end='     ')
    print(AverageWWT_SJF)
    print('---------------------------------------------------------------')


if __name__ == '__main__':
    if Algorithms == 1:
        FCFS()
    else:
        SJF()



































