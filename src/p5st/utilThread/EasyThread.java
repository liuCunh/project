package p5st.utilThread;

public class EasyThread {
    public static void main(String[] args) {
        SleepThread thread1 = new SleepThread("Thread A: ", 1000);
        SleepThread thread2 = new SleepThread("Thread B: ", 1500);
        SleepThread thread3 = new SleepThread("Thread C: ", 1200);
        thread1.start();
        thread2.start();
        thread3.start();

    }
}
class SleepThread extends Thread{
    private int time;
    public SleepThread(String name, int time){
        super(name);
        this.time = time;
    }

    @Override
    public void run() {
        try{
            Thread.sleep(time);  // 指定休眠时间
        }catch (InterruptedException e){
            e.printStackTrace();
        }
        System.out.println(Thread.currentThread().getName()+"休眠 "+time+" mile");
    }
}
