package p3st.util.car;

public class CarTest {
    public static void main(String[] args) {
        // 创建对象
        Bus bus = new Bus("川A·000001", 4);
        Truck truck = new Truck("京A·111111", 30);
        // 调用缴费方法
        bus.getMoney(150);
        truck.getMoney(150);
    }
}
