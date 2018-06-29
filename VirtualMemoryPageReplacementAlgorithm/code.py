# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 19:43:04 2018

@author: Terence
"""

n = 7                                               #页面数
m = 3                                               #物理块数
Pn = [4,3,2,1,4,3,5,4,3,2,1,5,6,2,3,7,1,2,6,1]      #序列
physical_block = [-1 for i in range(m)]             #物理块临时记录
page_fault_number = 0                               #缺页次数
page_fault_rate = 0.0                               #缺页率



def FIFO():
    '''
        先进先出页面置换算法
    '''
    
    #初始化数据
    global page_fault_number
    global physical_block
    global page_fault_rate
    line = []   #物理块记录
    
    #核心算法
    for temp in Pn:
        if temp in physical_block:      #已在物理块中的记为-1（代表没有缺页）
            line.append([-1,-1,-1])
        else:                           #将最早进入的页面换掉
            tem = physical_block[1]
            physical_block[1] = physical_block[0]
            physical_block[2] = tem
            physical_block[0] = temp
            line.append([temp,physical_block[1],tem])
            page_fault_number = page_fault_number + 1
    
    #结果输出
    print("-------------------------------------------------------------------")
    print("=====================FIFO：先进先出页面置换算法=====================")
    print("-------------------------------------------------------------------")
    for p in Pn:
        print(p,end="  ")
    print("-------------------------------------------------------------------")
    for l in line:
        if l[0] == -1:
            print("   ",end="")
        else:
            print(l[0],end="  ")
    print()
    for l in line:
        if l[1] == -1:
            print("   ",end="")
        else:
            print(l[1],end="  ")
    print()
    for l in line:
        if l[2] == -1:
            print("   ",end="")
        else:
            print(l[2],end="  ")
    print("-------------------------------------------------------------------")
    print("缺页次数： "+str(page_fault_number))
    page_fault_rate = (page_fault_number/len(Pn))*100
    print("缺页率： "+str(page_fault_rate)+"%")

    



def OPI():
    '''
        最佳页面置换算法
    '''
    #初始化数据
    global page_fault_number
    global physical_block
    global page_fault_rate
    physical_block = [-1 for i in range(m)]
    page_fault_number = 0
    page_fault_rate = 0.0
    line = []               #物理块记录
    distance = [0,0,0]      #记录最远使用距离
    
    #核心算法
    count = 0
    while count < len(Pn):
        if Pn[count] in physical_block:          #已在物理块中的记为-1（代表没有缺页）
            line.append([-1,-1,-1])
        else:
            if -1 in physical_block:            #如果有空闲的物理块，直接放入
                tem = physical_block[1]
                physical_block[1] = physical_block[0]
                physical_block[2] = tem
                physical_block[0] = Pn[count]
                line.append([physical_block[0],physical_block[1],physical_block[2]])
                page_fault_number = page_fault_number + 1
            else:                               #没有空闲的物理块，进行最佳页面置换算法
                #计算距离
                distance = [0,0,0]
                findit = Pn[count:]
                for it in findit:
                    if it == physical_block[0]:
                        break
                    else:
                        distance[0] = distance[0] + 1                 
                findit = Pn[count:]
                for it in findit:
                    if it == physical_block[1]:
                        break
                    else:
                        distance[1] = distance[1] + 1 
                findit = Pn[count:]
                for it in findit:
                    if it == physical_block[2]:
                        break
                    else:
                        distance[2] = distance[2] + 1 
                d = distance[:]
                d.sort()
                #把最晚使用的页面换出
                physical_block[distance.index(d[2])] = Pn[count]
                line.append([physical_block[0],physical_block[1],physical_block[2]])
                page_fault_number = page_fault_number + 1
        count = count + 1
    
    #输出结果
    print("-------------------------------------------------------------------")
    print("=====================OPI：最佳页面置换算法==========================")
    print("-------------------------------------------------------------------")
    for p in Pn:
        print(p,end="  ")
    print("-------------------------------------------------------------------")
    for l in line:
        if l[0] == -1:
            print("   ",end="")
        else:
            print(l[0],end="  ")
    print()
    for l in line:
        if l[1] == -1:
            print("   ",end="")
        else:
            print(l[1],end="  ")
    print()
    for l in line:
        if l[2] == -1:
            print("   ",end="")
        else:
            print(l[2],end="  ")
    print("-------------------------------------------------------------------")
    print("缺页次数： "+str(page_fault_number))
    page_fault_rate = (page_fault_number/len(Pn))*100
    print("缺页率： "+str(round(page_fault_rate,2))+"%")


def LRU():
    '''
        最近最久未使用页面置换算法
    '''
    
    #初始化数据
    global page_fault_number
    global physical_block
    global page_fault_rate
    physical_block = [-1 for i in range(m)]
    page_fault_number = 0
    page_fault_rate = 0.0
    line = []           #物理块记录
    distance = [0,0,0]  #最早使用的距离
    
    #核心算法
    count = 0
    while count < len(Pn):
        if Pn[count] in physical_block:         #已在物理块中的记为-1（代表没有缺页）
            line.append([-1,-1,-1])
        else:
            if -1 in physical_block:            #如果有空闲的物理块，直接放入
                tem = physical_block[1]
                physical_block[1] = physical_block[0]
                physical_block[2] = tem
                physical_block[0] = Pn[count]
                line.append([physical_block[0],physical_block[1],physical_block[2]])
                page_fault_number = page_fault_number + 1
            else:                               #没有空闲的物理块，进行最佳页面置换算法
                #计算最早使用的页面
                distance = [0,0,0]
                findit = list(reversed(Pn[:count]))
                for it in findit:
                    if it == physical_block[0]:
                        break
                    else:
                        distance[0] = distance[0] + 1                 
                findit = list(reversed(Pn[:count]))
                for it in findit:
                    if it == physical_block[1]:
                        break
                    else:
                        distance[1] = distance[1] + 1 
                findit = list(reversed(Pn[:count]))
                for it in findit:
                    if it == physical_block[2]:
                        break
                    else:
                        distance[2] = distance[2] + 1 
                d = distance[:]
                d.sort()
                #将最早使用的页面换出
                physical_block[distance.index(d[2])] = Pn[count]
                line.append([physical_block[0],physical_block[1],physical_block[2]])
                page_fault_number = page_fault_number + 1
        count = count + 1
    
    #输出结果
    print("-------------------------------------------------------------------")
    print("=====================LRU:最近最久未使用页面置换算法==================")
    print("-------------------------------------------------------------------")
    for p in Pn:
        print(p,end="  ")
    print("-------------------------------------------------------------------")
    for l in line:
        if l[0] == -1:
            print("   ",end="")
        else:
            print(l[0],end="  ")
    print()
    for l in line:
        if l[1] == -1:
            print("   ",end="")
        else:
            print(l[1],end="  ")
    print()
    for l in line:
        if l[2] == -1:
            print("   ",end="")
        else:
            print(l[2],end="  ")
    print("-------------------------------------------------------------------")
    print("缺页次数： "+str(page_fault_number))
    page_fault_rate = (page_fault_number/len(Pn))*100
    print("缺页率： "+str(round(page_fault_rate,2))+"%")





if __name__ == '__main__':
    #先进先出
    FIFO()
    #最佳置换
    OPI()
    #最近最近未使用
    LRU()