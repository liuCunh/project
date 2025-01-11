package p3st.util.car1;

public class CarTest {
    public static void main(String[] args) {
        Car busCar = new Bus("川A·000001", 2);
        Car truckCar = new Truck("京A·111111", 9.5);
        // 调用构造方法
        busCar.payMoney(98.26);
        truckCar.payMoney(96.25);
    }
}

//class TollStation {
//    // 多态方法
//    public void collectMoney(Car car, double distance){
//        System.out.println("收费站方法");
//        car.payMoney(distance);
//    }
//}

abstract class Car {
    protected String carno;  // 车牌号
    // 构造方法
    public Car(String carno){
        this.carno = carno;
    }

    public String getCarno() {
        return carno;
    }

    public void setCarno(String carno) {
        this.carno = carno;
    }

    // 缴费方法
    public abstract void payMoney(double distance);
}

class Truck extends Car {
    private double weight;  // 最大重量
    // 构造方法
    public Truck(String carno, double weight){
        super(carno);
        this.weight = weight;
    }
    // 支付方法
    public void payMoney(double distance){
        double temp = weight < 2000 ? distance*0.9 : distance*1.6;
        System.out.println("-------------truck init-------------");
        System.out.printf("车辆 %s，核载重量：%.2f，缴费金额：%.2f\n", carno, weight, temp);
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }
}
class Bus extends Car {
    protected int passengers;  // 核载人数
    public Bus(String carno, int passengers) {
        super(carno);
        this.passengers = passengers;
    }
    // 支付方法
    public void payMoney(double distance){
        double temp = passengers<19 ? distance*0.6 : distance*0.9;
        System.out.println("-------------Bus init-------------");
        System.out.printf("车辆 %s，核载人数：%d，缴费金额：%.2f\n", carno, passengers, temp);
    }

    public int getPassengers() {
        return passengers;
    }

    public void setPassengers(int passengers) {
        this.passengers = passengers;
    }
}