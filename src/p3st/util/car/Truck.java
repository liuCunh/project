package p3st.util.car;

public class Truck extends Car {
    private double weight;  // 荷载重量
    // 初始化
    public Truck(String carno, double weight) {
        super(carno);
        this.weight = weight;
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }
    // 缴费方法重写
    public void getMoney(double roadLength){
        double money = 0;
        if(weight > 4000){
            money += (1.6*roadLength);
        }else if(2000 <= weight && weight <= 4000){
            money += (1.2*roadLength);
        }else{
            money += (0.9*roadLength);
        }
        System.out.printf("车辆 %s 正在缴费! 缴纳费用为：%.2f元\n", getCarno(),  money);
    }
}
