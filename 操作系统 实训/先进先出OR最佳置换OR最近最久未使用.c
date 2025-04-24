#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
 
const int MaxNumber=100;
int PageOrder[MaxNumber];  //页面序列
int PageNum,LackNum,MinBlockNum;  //页面个数，缺页次数,最小物理块数
int PageDisCount[MaxNumber]; //当前内存距离下一次出现的距离
int LRUtime[MaxNumber];   //存储队列中各个页面最近使用情况
 
double  LackPageRate;   //缺页率
int LackPageNum;   //缺页数
int VirtualQueue[MaxNumber];   //虚拟队列
 
void input();
void initial();
void FIFO();    //先进先出
void OPI();     //最佳置换
void LRU();    //最近最久未使用LRU页面置换算法
void display();
 
void input()
{
        ifstream readData;
        readData.open("data.txt");
        readData>>MinBlockNum;
        readData>>PageNum;
        int i;
        for (i=0;i<PageNum;i++)
        {
                readData>>PageOrder[i];
        }
 
        cout<<"读取数据结果如下："<<endl;
        cout<<"最小物理块数 = "<<MinBlockNum<<endl;
        cout<<"页面个数 = "<<PageNum<<endl;
        cout<<"页面序列如下:"<<endl;
        for (i = 0;i<PageNum;i++)
        {
                cout<<PageOrder[i]<<" ";
        }
        cout<<endl;
}
 
void initial()
{
        LackPageNum = MinBlockNum;
        LackPageRate = 0.0;
        int i,j,k;
 
        for(i = 0;i<PageNum;i++)
        {
                PageDisCount[i] = 0;  //初始化距离都为0
                VirtualQueue[i] = -1;  //初始化队列的值都为负数
        }
 
        for (i = 0;i<MinBlockNum;i++)
        {
                bool isInQueue2 = false;
                int dis = 0;
                LRUtime[i] = 0;
                for (j = 0;j<MinBlockNum;j++)
                {
                        if (VirtualQueue[j] == PageOrder[i])
                        {
                                isInQueue2 = true;
                        }
                }
                if (!isInQueue2)  //当有新的进程进入到队列时，便计算其对应的距离
                {
                        VirtualQueue[i] = PageOrder[i];
                        for (k = 0;k<i;k++)
                        { 
                                LRUtime[k]++;   //之前的页面对应的时间+1
                        }
                        display();
                }
                else
                {
                        LRUtime[i] = 0;  //重新更新为0，表示最近刚刚使用
                }

        }
}
 
void FIFO()
{
        cout<<"********* 你选择了FIFO算法：********* "<<endl;
        cout<<"页面置换情况如下:"<<endl;
        initial();
        bool isInQueue;
        int point = 0;  //指向最老的页面
        int i,k;
        for (i = MinBlockNum;i<PageNum;i++)
        {
                isInQueue = false;
                for (k = 0;k<MinBlockNum;k++)
                {
                        if (VirtualQueue[k] == PageOrder[i])   //如果当前页面在队列中
                        {
                                isInQueue = true;
                        }
                }
 
                if (!isInQueue)   //如果当前页面不在队列中，则进行相应的处理
                {
                        LackPageNum++;  //缺页数加1
 
                        VirtualQueue[point] = PageOrder[i];
                        display();
                        point++;
                        if (point == MinBlockNum) 
                        {
                                point = 0;  //当point指向队尾后一位的时候，将point重新指向队首
                        }
                }
        }
 
        LackPageRate = (LackPageNum * 1.0)/PageNum;
        cout<<"缺页数LackPageNum = "<<LackPageNum<<endl;
        cout<<"缺页率LackPageRate = "<<LackPageRate<<endl;

}
 
void OPI()
{
        cout<<"********* 你选择了OPI算法：********* "<<endl;
        cout<<"页面置换情况如下:"<<endl;
        initial();
            
        bool isInQueue;
        int dis;   //表示队列每个值距离下一次访问的距离
        int point;  //指向最长时间未被访问的下标
        int i,k,s,t,m;
        for(int i = MinBlockNum;i<PageNum;i++)
        {
                isInQueue = false;
                for (k = 0;k<MinBlockNum;k++)
                {
                        if (VirtualQueue[k] == PageOrder[i])   //如果当前页面在队列中
                        {
                                isInQueue = true;
                        }
                }
 
                if (!isInQueue)
                {
                        LackPageNum++;
                        //计算当前队列每一页对应的下一次出现的距离
                        for (s = 0;s < MinBlockNum;s++)
                        {
                                dis = 1;
                                for (t = i;t<PageNum;t++)   //从页面序列的第i个位置开始找起
                                {
                                        if (VirtualQueue[s] != PageOrder[t])
                                        {
                                                dis++;
                                        }
                                        else
                                        {
                                                break;
                                        }
                                }
                                PageDisCount[s] = dis;

                        }
                        point = 0;
                        for (m = 1;m < MinBlockNum;m++)
                        {
                                if (PageDisCount[point] < PageDisCount[m])
                                {
                                        point = m;
                                }
                        }
 
 
                        VirtualQueue[point] = PageOrder[i];
                        display();
 
                }//if
        }//for
 
        LackPageRate = (LackPageNum*1.0)/PageNum;
        cout<<"缺页数LackPageNum = "<<LackPageNum<<endl;
        cout<<"缺页率LackPageRate = "<<LackPageRate<<endl;
}
 
void LRU()
{
        cout<<"********* 你选择了LRU算法：********* "<<endl;
        cout<<"页面置换情况如下:"<<endl;
 
        initial();
        bool isInQueue;
        int point,k;  //指向最长时间未被访问的下标
        int i,s,j;
        for(int i = MinBlockNum;i<PageNum;i++)
        {
                isInQueue = false;
                for (k = 0;k<MinBlockNum;k++)
                {
                        if (VirtualQueue[k] == PageOrder[i])   //如果当前页面在队列中
                        {
                                isInQueue = true;
                        }
                }
 
                if (!isInQueue)
                {
                        LackPageNum++;
                        point = 0;
                        for (j = 1;j<MinBlockNum;j++)
                        {
                                if (LRUtime[point]<LRUtime[j])
                                {
                                        point = j;
                                }
                        }
 
                        for (s = 0;s<MinBlockNum;s++)//其余页面对应的时间要+1
                        {
                                if (VirtualQueue[s] != VirtualQueue[point])
                                {
                                        LRUtime[s]++;
                                }
                        }
 
                        VirtualQueue[point] = PageOrder[i];
                        LRUtime[point] = 0;
 
                        display();
                }//if
                else   //负责更新当前对应页面的时间
                {
                        for (s = 0;s<MinBlockNum;s++)//其余页面对应的时间要+1
                        {
                                if (VirtualQueue[s] != PageOrder[i])
                                {
                                        LRUtime[s]++;
                                }
                                else
                                        LRUtime[s] = 0;
                        }
                }
        }//for
 
        LackPageRate = (LackPageNum*1.0)/PageNum;
        cout<<"缺页数LackPageNum = "<<LackPageNum<<endl;
        cout<<"缺页率LackPageRate = "<<LackPageRate<<endl;
}
 
void display()
{       int i;
        for (i = 0;i<MinBlockNum && VirtualQueue[i]>=0;i++)
        {
                cout<<VirtualQueue[i]<<" ";
        }
        cout<<endl;
}
 
int main()
{
        input();
 
        int isContinue = 1;
        int chooseAlgorithm;
 
        while(isContinue)
        {
                cout<<"******************************************************"<<endl;
                cout<<"********* 请选择算法    **********"<<endl;
                cout<<"********* 1代表FIFO算法 **********"<<endl;
                cout<<"********* 2代表OPI算法  **********"<<endl;
                cout<<"********* 3代表LRU算法  **********"<<endl;
                cin>>chooseAlgorithm;
                switch(chooseAlgorithm)
                {
                case 1:
                        FIFO();
                        break;
                case 2:
                        OPI();
                        break;
                case 3:
                        LRU();
                        break;
                default:
                        cout<<"请输入正确的序号进行选择："<<endl;break;
                }
                cout<<"********** 是否继续选择算法?              **********"<<endl;
                cout<<"********** 输入1代表继续，输入0代表退出！ **********"<<endl;
                cin>>isContinue;
        }
 
        cout<<"***************************结束***************************"<<endl;
 
//      system("pause");
 
        return 0;
}
