# -*- coding: utf-8 -*-

n = 10
track_list = [78,30,9,15,102,140,156,54,45,125]
m = 100
direction = True #True=正 False=反
distance = []
average = 0.0

def FCFS():
    '''
        先来先服务
    '''
    distance = []
    average = 0.0
    temp = m
    for track in track_list:
        distance.append(abs(temp-track))
        temp = track
    print("-------------------------------------------------------------")
    print("========================FCFS先来先服务========================")
    print("-------------------------------------------------------------")
    print("磁道  | 寻道长度 ")
    print("----------------")
    count = 0
    for track in track_list:
        print(track,end="")
        if track<10:
            print("",end="     |  ")
        elif track>99:
            print("",end="   |  ")
        else:
            print("",end="    |  ")
        print(distance[count])
        count += 1
    print("----------------")
    average = sum(distance)/10
    print("平均寻道长度：",str(average))

def SSTF():
    '''
        最短寻道时间优先
    '''
    distance = []
    average = 0.0
    theList = []
    temp_list = track_list[:]
    temp_list.sort()
    temp = m
    z = 0
    while z<n:
        count = 0
        for x in temp_list:
            if m<x:
                break
            count += 1
        if count==0:
            theList.append(temp_list[0])
            distance.append(abs(temp-temp_list[0]))
            temp = temp_list[0]
            temp_list.remove(temp_list[0])
            break
        pre = temp-temp_list[count-1]
        if count<len(temp_list):
            last = temp_list[count]-temp
            if pre<last:
                theList.append(temp_list[count-1])
                distance.append(abs(temp-temp_list[count-1]))
                temp = temp_list[count-1]
                temp_list.remove(temp_list[count-1])
            else:
                theList.append(temp_list[count])
                distance.append(abs(temp-temp_list[count]))
                temp = temp_list[count]
                temp_list.remove(temp_list[count])
        else:
                theList.append(temp_list[count-1])
                distance.append(abs(temp-temp_list[count-1]))
                temp = temp_list[count-1]
                temp_list.remove(temp_list[count-1])
        z += 1
    print("-------------------------------------------------------------")
    print("==================SSTF最短寻道时间优先========================")
    print("-------------------------------------------------------------")
    print("磁道  | 寻道长度 ")
    print("----------------")
    count = 0
    for track in theList:
        print(track,end="")
        if track<10:
            print("",end="     |  ")
        elif track>99:
            print("",end="   |  ")
        else:
            print("",end="    |  ")
        print(distance[count])
        count += 1
    print("----------------")
    average = sum(distance)/10
    print("平均寻道长度：",str(average))
    
def SCAN():
    '''
        扫描
    '''
    distance = []
    average = 0.0
    theList =[]
    temp_list = track_list[:]
    temp_list.sort()
    temp = m
    count = 0
    for x in temp_list:
        if m<x:
            break
        count += 1
    if direction==True:
        while count<n:
            theList.append(temp_list[count])
            count += 1
        for the in theList:
            temp_list.remove(the)
        temp_list.reverse()
        theList.extend(temp_list)
        for x in theList:
            distance.append(abs(x-temp))
            temp = x
    else:
        while count+1>0:
            theList.append(temp_list[count])
            count = count - 1
        for the in theList:
            temp_list.remove(the)
        theList.extend(temp_list)
        for x in theList:
            distance.append(abs(x-temp))
            temp = x
    print("-------------------------------------------------------------")
    print("==================SCAN扫描===================================")
    print("-------------------------------------------------------------")
    print("磁道  | 寻道长度 ")
    print("----------------")
    count = 0
    for track in theList:
        print(track,end="")
        if track<10:
            print("",end="     |  ")
        elif track>99:
            print("",end="   |  ")
        else:
            print("",end="    |  ")
        print(distance[count])
        count += 1
    print("----------------")
    average = sum(distance)/10
    print("平均寻道长度：",str(average))

def CSCAN():
    '''
        循环扫描
    '''
    distance = []
    average = 0.0
    theList =[]
    temp_list = track_list[:]
    temp_list.sort()
    temp = m
    count = 0
    for x in temp_list:
        if m<x:
            break
        count += 1
    if direction==True:
        while count<n:
            theList.append(temp_list[count])
            count += 1
        for the in theList:
            temp_list.remove(the)
        theList.extend(temp_list)
        for x in theList:
            distance.append(abs(x-temp))
            temp = x
    else:
        while count+1>0:
            theList.append(temp_list[count])
            count = count - 1
        for the in theList:
            temp_list.remove(the)
        temp_list.reverse()
        theList.extend(temp_list)
        for x in theList:
            distance.append(abs(x-temp))
            temp = x
    print("-------------------------------------------------------------")
    print("==================CSCAN扫描==================================")
    print("-------------------------------------------------------------")
    print("磁道  | 寻道长度 ")
    print("----------------")
    count = 0
    for track in theList:
        print(track,end="")
        if track<10:
            print("",end="     |  ")
        elif track>99:
            print("",end="   |  ")
        else:
            print("",end="    |  ")
        print(distance[count])
        count += 1
    print("----------------")
    average = sum(distance)/10
    print("平均寻道长度：",str(average))
    

if __name__ == '__main__':
    FCFS()
    SSTF()
    SCAN()
    CSCAN()