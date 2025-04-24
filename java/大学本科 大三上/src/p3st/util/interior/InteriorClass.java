package p3st.util.interior;

public class InteriorClass {
    public static void main(String[] args) {
        Computer computer = new Computer();
        // 创建 USB 内部类
        USB usb = new USB(){
            @Override
            public void connect(){
                System.out.println("USB插入！");
            }
            @Override
            public void unconnect(){
                System.out.println("USB拔出！");
            }
        };
        computer.useUSB(usb);
    }
}
// USB的接口--插入、拔出方法
interface USB{
    public void connect();
    public void unconnect();
}
class Computer{
    public void start(){
        System.out.println("电脑启动！");
    }
    public void connect(){
        System.out.println("插入USB");
    }
    // 传入接口类，使得传入多个不同对象（键盘对象、鼠标对象）时不会出现类型错误
    public void useUSB(USB usb){
        usb.connect();
        usb.unconnect();
    }
}