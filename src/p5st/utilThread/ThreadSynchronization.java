package p5st.utilThread;
/**
 * 某电影院正在上映国产大片，共有100张票，它有3个窗口售票，请设计一个程序模拟该电影院卖票。
 * 不能漏票
 * 不能卖出重复票
 * 不能卖出无效票
 * */
public class ThreadSynchronization {
    public static void main(String[] args) {
        MyRunnable mr = new MyRunnable();  // 生成任务对象

        // 开启三个线程窗口同时卖票
        Thread t1 = new Thread(mr, "窗口 1 ");
        Thread t2 = new Thread(mr, "窗口 2 ");
        Thread t3 = new Thread(mr, "窗口 3 ");
        t1.start();
        t2.start();
        t3.start();
    }

}
class MyRunnable implements Runnable{
    private int ticket = 0;  // 共享数据，票的数量 临界资源
    @Override
    public void run(){
        // 若将整个while循环作为 临界区 那么在程序运行时，哪一个进程抢到，就有那一个进程全部执行操作。
        while (true){
            if (sale()) break;
        }
    }

    private synchronized boolean sale() {
        // 临界区
        if (ticket < 100){
            // 没有卖到100张票
            try{
                Thread.sleep(10);  // 模拟出票延时
            } catch(InterruptedException e){
                e.printStackTrace();
            }
            ticket++;
            String window = Thread.currentThread().getName();  // 获取买票窗口
            System.out.println(window + "正在卖第 " + ticket + " 张票");
        }else{
            // 100张票已经买完
            return true;
        }
        return false;
    }
}
