package p5st.utilThread;

public class ThreeTeacher {
    public static void main(String[] args) {
        TeacherRunnable tr = new TeacherRunnable();
        Thread t1 = new Thread(tr, "李");
        Thread t2 = new Thread(tr, "王");
        Thread t3 = new Thread(tr, "张");
        t1.start();
        t2.start();
        t3.start();
    }

}

class TeacherRunnable implements Runnable{
    private int notes = 100;  // 笔记数量

    @Override
    public void run() {
        while(true){
            if (send()) break;
        }
    }

    private synchronized boolean send() {
        if(notes > 0) {
            try {
                Thread.sleep(10);  // 模式发布作业耗时
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName() + "老师 正在发送第 " + (101 - notes) + " 篇笔记");
            notes--;
        }else {
            return true;
       }
        return false;
    }
}