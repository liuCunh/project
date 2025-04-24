package p5st.utilThread;

import static java.lang.Thread.sleep;

public class ThreadCreate {
    /*
    * 从小到大输出大写字母，输出后停顿0.1s
    * */
    public static void main(String[] args) {
        // Runnable实现
        Run1 r1 = new Run1();
        Thread thread = new Thread(r1);
        thread.start();

        // Thread实现
        Run2 r2 = new Run2();
        r2.start();

        // 匿名函数实现
        Thread t = new Thread(() ->{
            for(int i = 1; i<10; i++){
                System.out.println(Thread.currentThread().getName()+ " " + i);
            }
        });
        t.start();
    }
}
// 通过Runnable接口创建线程
class Run1 implements Runnable{
    @Override
    public void run(){
        for(char i = 'A'; i<='Z'; i++){
            System.out.println(i);
            try{
                sleep(100);
            }catch (InterruptedException e){
                throw new RuntimeException(e);
            }
        }
    }
}
// 通过继承Thread类实现接口
class Run2 extends Thread{
    @Override
    public void run(){
        for(char i = 'A'; i<='Z'; i++){
            System.out.println(i);
            try{
                sleep(100);
            }catch (InterruptedException e){
                throw new RuntimeException(e);
            }
        }
    }
}
