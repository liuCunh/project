package p3st.util.car;

public class Bus extends Car {
    private int count;  // 荷载人数
    // 初始化
    public Bus(String carno, int count) {
        super(carno);
        this.count = count;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }
    // 缴费方法重写
    public void getMoney(double roadLength){
        double money = 0;
        if(count>=19){
            money += (0.9*roadLength);
        }else {
            money += (0.6*roadLength);
        }
        System.out.printf("车辆 %s 正在缴费! 缴纳费用为：%.2f元\n", getCarno(),  money);
    }
}
