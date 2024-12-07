 #include <stdio.h>
 #include <stdlib.h>
 #include <unistd.h>
 #include <pthread.h>
 #include <semaphore.h>
 #define NUM 5
 int queue[NUM];  // 等待队列 长度为 5
 sem_t blank_number,product_number, mutex;  // blank_number为empty信号量, product_number为full信号量
 
 
 // 生产者进程
 void * producer(void *arg)
 {
 int i=0;
 while (1) {
	 
 sem_wait(&blank_number);  // P操作,申请empty信号量
 sem_wait(&mutex);  // P操作, 申请mutex信号量
 
 // 临界区开始
 queue[i]=rand()%1000+1;  // 生产商品编号
 printf("----Producer---%d\n",queue[i]);
 // 临界区结束
 
 sem_post(&mutex);  // V操作, 释放mutex信号量
 sem_post(&product_number);  // V操作 释放full信号量
 i=(i+1)%NUM;  // 队列索引
 sleep(rand()%2);  // 随机等待时间
      }
 }
 
 
 // 消费者进程
 void * consumer(void *arg)
 {
 int i=0;
 while (1) {
	 
 sem_wait(&product_number);  // P操作 申请full信号量
 sem_wait(&mutex);  // P操作, 申请mutex信号量
 
 // 临界区开始
  printf("----Consume---%d\n",queue[i]);
  queue[i]=0;  // 消耗商品编号
  // 临界区结束
  
 sem_post(&mutex);  // V操作, 释放mutex信号量
 sem_post(&blank_number);  // V操作 释放empty信号量
 i=(i+1)%NUM;  // 队列索引
 sleep(rand()%2);  // 随机等待时间
      }
 }
 
 
 int main(int argc, char *argv[])
 {
     pthread_t pid, cid;
    sem_init(&blank_number,0,NUM);  // 初始化 empty=5 信号量, 在使用信号量之前需要先初始化,将变量初始化为信号量
    sem_init(&product_number,0,0);  // 初始化 full=0 信号量
	sem_init(&mutex, 0, 1);  // 初始化 mutex=1 互斥信号量
     pthread_create(&pid, NULL, producer, NULL);  // 创建生产者进程
     pthread_create(&cid, NULL, consumer, NULL);  // 创建消费者进程
     pthread_join(pid, NULL);  // 执行生产者进程
     pthread_join(cid, NULL);  // 执行消费者进程
     sem_destroy(&blank_number);  // 销毁empty信号量
     sem_destroy(&product_number);  // 销毁full信号量
	 sem_destroy(&mutex);  // 销毁mutex信号量
     return 0;
 }
