package p3st.util.usb1;

public class USBTest {
    public static void main(String[] args) {
        Computer computer = new Computer();
        computer.useUSB(new Mouse());  // 使用鼠标方法
        System.out.println("---------- 分隔符 ----------");
        computer.useUSB(new KeyBorad());// 使用键盘方法
    }
}
// USB的接口--插入、拔出方法
interface USB{
    public void connect();
    public void unconnect();
}
// 键盘类
class KeyBorad implements USB {
    @Override
    public void connect(){
        System.out.println("键盘插入！");
    }
    @Override
    public void unconnect(){
        System.out.println("键盘拔出！");
    }
}
// 鼠标类
class Mouse implements USB {
    @Override
    public void connect(){
        System.out.println("鼠标插入!");
    }
    @Override
    public void unconnect(){
        System.out.println("鼠标拔出!");
    }
}
// 电脑类
class Computer{
    public void start(){
        System.out.println("电脑启动！");
    }
    public void connect(){
        System.out.println("插入USB");
    }
    // 传入接口类，使得传入多个不同对象（键盘类、鼠标类）时不会出现类型错误
    public void useUSB(USB usb){
        usb.connect();
        usb.unconnect();
    }
}