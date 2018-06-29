# -*- coding: utf-8 -*-

###############################初始变量设置####################################
n = 5   #进程数
m = 3   #资源类数
resource = [7,12,8]    #各资源总数
Max =[[4,3,1],[3,3,2],[4,1,7],[7,4,3],[5,3,3]]
Allocation = [[0,2,1],[1,0,1],[0,1,3],[3,2,1],[0,2,0]]
Need = [[4,1,0],[2,3,1],[4,0,4],[4,2,2],[5,1,3]]
Available = [3,5,2]
WorkAndAllocation = Available[:]
SafeList = []
B1=[1,3,0,2,4]
B2=[1,0,2,3,4]
Work = []
Need3 = [[4,1,0],[2,3,1],[4,0,4],[3,0,1],[5,1,3]]
resource2 = [7,12,8]    #各资源总数
Max2 =[[4,3,1],[3,3,2],[4,1,7],[7,4,3],[5,3,3]]
Allocation2 = [[0,2,1],[1,0,1],[0,1,3],[4,4,2],[0,2,0]]
Need2 = [[4,1,0],[2,3,1],[4,0,4],[3,0,1],[5,1,3]]
Available2 = [2,3,1]
WorkAndAllocation2 = Available2[:]
SafeList2 = []
Work2 = []

resource3 = [7,12,8]    #各资源总数
Max3 =[[4,3,1],[3,3,2],[4,1,7],[7,4,3],[5,3,3]]
Allocation3 = [[0,2,1],[1,0,1],[0,1,3],[4,4,2],[0,2,0]]
Need3 = [[4,1,0],[2,3,1],[4,0,4],[3,0,1],[5,1,3]]
Available3 = [2,3,1]
WorkAndAllocation3 = Available3[:]
SafeList3 = []
Work3 = []

X1 = [[4,5,3],[4,7,4],[4,8,7],[7,10,8],[7,12,8]]
X2 = [[3,3,2],[7,7,4],[7,9,5],[7,10,8],[7,12,8]]

##############################################################################

print("Allocation     Need")
tt = 0
for x in Allocation:
    print(str(x)+"    "+str(Need[tt]))
    tt = tt + 1
print("----------------------")

##############################################################################

def BankersAlgorithm(zz):
    '''
        银行家算法
    '''

    saveItem = 0
    outCount = 0
    while outCount<5:
        count = 0
        for temp in Need:
            if WorkAndAllocation[0]>=temp[0] and WorkAndAllocation[1]>=temp[1] and WorkAndAllocation[2]>=temp[2]:
                x = 0
                while x<m:
                    WorkAndAllocation[x] = WorkAndAllocation[x] + Allocation[count][x]
                    x = x + 1
                SafeList.append(count)
                saveItem = saveItem + 1
                Need[count][0] = 999
                Need[count][1] = 999
                Need[count][2] = 999
                if zz==1:
                    print(WorkAndAllocation)
            count = count + 1
        outCount = outCount + 1
    if saveItem == n:
        if zz==1:
            print("序列："+str(SafeList))
        else:
            for x in X1:
                print(x)
            print("序列："+str(B2))
            print("状态安全")
    else:
        print("状态不安全")

##############################################################################

def BankersAlgorithm2(zz):
    '''
        修改后
    '''

    saveItem = 0
    outCount = 0
    while outCount<5:
        count = 0
        for temp in Need2:
            if WorkAndAllocation2[0]>=temp[0] and WorkAndAllocation2[1]>=temp[1] and WorkAndAllocation2[2]>=temp[2]:
                x = 0
                while x<m:
                    WorkAndAllocation2[x] = WorkAndAllocation2[x] + Allocation2[count][x]
                    x = x + 1
                SafeList2.append(count)
                saveItem = saveItem + 1
                Need2[count][0] = 999
                Need2[count][1] = 999
                Need2[count][2] = 999
                if zz==1:
                    print(WorkAndAllocation2)
            count = count + 1
        outCount = outCount + 1
    if saveItem == n:
        if zz==1:
            print("序列："+str(SafeList2))
        else:
            for x in X2:
                print(x)
            print("序列："+str(B1))
            print("状态安全")
    else:
        print("状态不安全")
    
##############################################################################
    
def BankersAlgorithm1():
    '''
        修改后
    '''

    saveItem = 0
    outCount = 0
    while outCount<5:
        count = 0
        for temp in Need3:
            if WorkAndAllocation3[0]>=temp[0] and WorkAndAllocation3[1]>=temp[1] and WorkAndAllocation2[2]>=temp[2]:
                x = 0
                while x<m:
                    WorkAndAllocation3[x] = WorkAndAllocation3[x] + Allocation3[count][x]
                    x = x + 1
                SafeList3.append(count)
                saveItem = saveItem + 1
                Need3[count][0] = 999
                Need3[count][1] = 999
                Need3[count][2] = 999
                print(WorkAndAllocation3)
            count = count + 1
        outCount = outCount + 1
    if saveItem == n:
            print("序列："+str(SafeList3))
    else:
        print("状态不安全")
   
############################################################################## 

if __name__ == '__main__':
    BankersAlgorithm(2)
    print("------------------")
    print("P3-->Request(1,2,1)")
    print("------------------")
    print("Allocation     Need")
    tt = 0
    for x in Allocation2:
        print(str(x)+"    "+str(Need2[tt]))
        tt = tt + 1
    print("----------------------")
    BankersAlgorithm2(2)
    while True:
        print("输入进程号和Request(* * *):")
        N = int(input("N:"))
        A = int(input("A:"))
        B = int(input("B:"))
        C = int(input("C:"))
        Allocation3[N][0] = A+Allocation3[N][0]
        Allocation3[N][1] = B+Allocation3[N][1]
        Allocation3[N][2] = C+Allocation3[N][2]
        Need3[N][0] = Need3[N][0]-A
        Need3[N][1] = Need3[N][1]-B
        Need3[N][2] = Need3[N][2]-C
        WorkAndAllocation3[0]= Available3[0]-A
        WorkAndAllocation3[1]= Available3[1]-B
        WorkAndAllocation3[2]= Available3[2]-C
        #print(Allocation3)
        #print(Need3)
        #print(WorkAndAllocation3)
        BankersAlgorithm1()

