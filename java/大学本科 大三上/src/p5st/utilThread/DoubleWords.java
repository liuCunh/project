package p5st.utilThread;

public class DoubleWords {
    public static void main(String[] args) {
        A a = new A();
        B b = new B();
        a.start();
        b.start();
    }
}
// 临界资源
class SC{
    static boolean flag = false;  // 资源标志
    static int word = 10;  // 空位数
    static Object lock = new Object();
}

// 生产者
class A extends Thread{
    @Override
    public void run() {
        while (true){
            synchronized(SC.lock){
                if (SC.word==0){
                    break;
                }else{
                    // 是否含有数据
                    if(SC.flag){
                        try {
                            SC.lock.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }else{
                        System.out.print("A");
                        SC.flag = true;
                        SC.lock.notify();
                    }
                }
            }
        }
    }
}

class B extends Thread{
    @Override
    public void run() {
        while (true){
            synchronized(SC.lock){
                if (SC.word==0){
                    break;
                }else{
                    if(SC.flag){
                        System.out.print("B");
                        SC.word--;
                        SC.flag=false;
                        SC.lock.notify();
                    }else{
                        try{
                            SC.lock.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
            }
        }
    }
}
