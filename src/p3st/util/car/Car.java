package p3st.util.car;

public class Car {
    private String carno;  // 车牌号
    // 构造方法
    public Car(String carno) {
        this.carno = carno;
    }

    public String getCarno() {
        return carno;
    }

    public void setCarno(String carno) {
        this.carno = carno;
    }
    // 缴费方法
    public void getMoney(double roadLength){
        System.out.printf("车辆 %s 正在缴费!元\n", carno);
    }
}
