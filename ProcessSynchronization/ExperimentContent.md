**《操作系统》实验二内容要求**

【**实验题目**】**：**进程同步

【**实验学时**】：4学时

【**实验目的**】 

通过这次实验，加深对进程同步概念的理解，进一步掌握进程同步机制、进程同步算法和进程同步的评价。

【**实验内容**】

**问题描述：**

以生产者消费者模型为基础，在Windows环境下创建一个控制台进程（或者界面进程），在该进程中创建读者写者线程模拟生产者和消费者。写者线程写入数据，然后将数据放置在一个空缓冲区中供读者线程读取。读者线程从缓冲区中获得数据，然后释放缓冲区。当写者线程写入数据时，如果没有空缓冲区可用，那么写者线程必须等待读者线程释放出一个空缓冲区。当读者线程读取数据时，如果没有满的缓冲区，那么读入线程将被阻塞，直到新的数据被写进去。

**实现提示：**

本实验要求设计并实现一个进程，该进程拥有一个生产者线程和一个消费者线程，它们使用N个不同的缓冲区（N为一个确定的数值，本实验中取N=16）。你需要使用如下信号量：

一个互斥信号量mutex，用以阻止生产者线程和消费者线程同时操作缓冲区列表；

一个信号量full，当生产者线程生产出一个物品时可以用它向消费者线程发出信号；

一个信号量empty，消费者线程释放出一个空缓冲区时可以用它向生产者线程发出信号；

 

**实验要求：**

1)上机前认真复习进程同步算法，熟悉进程同步过程中进程的执行顺序和互相制约；

2)上机时独立编程、调试程序；

3)根据具体实验要求，完成好实验报告（包括实验的目的、内容、要求、源程序、实例运行结果截图）。