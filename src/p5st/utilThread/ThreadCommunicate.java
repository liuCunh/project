package p5st.utilThread;

/**
 * 要求生产者产生一个数字，消费者取得一个数字，一共产生10个数字
 * 不能出现生产者太快，或消费者太快的情况
 * */
public class ThreadCommunicate {
    public static void main(String[] args) {
        Producer p = new Producer();
        Consumer c = new Consumer();

        p.setName("生产者");
        c.setName("消费者");

        p.start();
        c.start();
    }
}

// 以下为生产者-消费者模型
// 临界区
class Box{
    static boolean flag = false;  // 临界区中是否有资源
    static int count=10;  // 总个数，共享数据
    static Object lock = new Object();  // 锁对象，锁对象必须唯一
}

// 生产者
/*
* 1.循环
* 2.同步代码块
* 3.判断共享数据是否到了末尾（到了末尾）
* 4.判定共享数据是否到了末尾（没到末尾就执行核心代码）
* */
class Producer extends Thread{
    @Override
    public void run() {
        while(true){
            synchronized(Box.lock){
                // 是否到了末尾
                if(Box.count == 0){
                    break;
                }else{
                    // 判断盒子中是否存在数据
                    if(Box.flag){
                        // 盒子中有数据, 等待
                        try {
                            Box.lock.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }else{
                        try {
                            sleep(100);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }

                        // 没有数据就生产数据
                        System.out.println(getName()+" : "+Box.count);
                        Box.flag = true;  // 标识生产成功
                        Box.lock.notify();  // 通知消费者取数据
                    }


                }
            }
        }
    }
}

// 消费者
/*
 * 1.循环
 * 2.同步代码块
 * 3.判断共享数据是否到了末尾（到了末尾）
 * 4.判定共享数据是否到了末尾（没到末尾就执行核心代码）
 * */
class Consumer extends Thread{
    @Override
    public void run() {
        while(true){
            synchronized(Box.lock){
                if(Box.count == 0){
                    break;
                }else{
                    // 判断盒子中是否存在数据
                    if(Box.flag){
                        try {
                            sleep(100);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        // 盒子中存在数据
                        System.out.println(getName()+" : "+Box.count);
                        Box.count--;  // 取数据
                        Box.flag=false;  // 标志为空
                        Box.lock.notify();  // 通知生产这
                    }else{
                        // 盒子中不存在数据
                        try {
                            Box.lock.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
            }
        }
    }
}