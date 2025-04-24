package p5st.utilThread;
/**
 * 线程的先后执行 和 线程的同步操作
 * 模拟新年的钟声倒计时10秒，即在屏幕上依次输出10、9、8、7、6、5、4、3、2、1
 * 共10个数字，每输出一个数字停顿1秒再输出下一个数字。
 * 倒计时开始之前打印“开始计时”，倒计时结束后在屏幕上打印“时间到”
 * 倒计时5秒后停止倒计时并在屏幕上打印“停”
 * */
public class ThreadSchedule {
    public static void main(String[] args) {
        System.out.println("开始计时");
        MyThread t = new MyThread();
        t.start();
//        // 程序优先级，让 子线程（t线程）结束之后 主线程才开始运行
//        // 线程异步， 在主线程开始调用子线程时，先让子线程做完操作（等待10s）后，主线程才继续执行
//        try{
//            t.join();  // 等待线程结束
//        }catch (InterruptedException e){
//            e.printStackTrace();
//        }
//        System.out.println("时间到！");

        // 循环5次之后直接结束，通过进程放置直接break结束
        // 主线程ThreadSchedule中的main方法跟 子线程t线程 同步计时，当子线程和主线程在同时运行在执行5s后终止
        try {
            Thread.sleep(5000);  // 线程休眠5s
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        t.interrupt();  // 子线程t线程终止
        System.out.println("\n停！");
    }
}

// 输出数字
class MyThread extends Thread{
    @Override
    public void run() {
        for(int i=10; i>0; i--){
            System.out.print(i + " ");
            try{
                sleep(1000);
            }catch(InterruptedException e){
//                e.printStackTrace();  // 当sleep方法遇上interrupt指令时， 抛出InterruptedException错误
//                System.out.println("强行休眠！");
                break;  // 结束循环
            }
        }
    }
}
