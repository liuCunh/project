package p3st.util.lamdbaUse;

public class LamdabClass {
    // 使用lambda创建对象
    /*
    PayInterface weixin1 = new PayInterface() {
        @Override
        public void payMoney(double money) {
            System.out.println("微信支付，支付金额"+money);
        }
    };
    两个等价
    */
    PayInterface weixin = money -> {
        System.out.println("微信支付，支付金额"+money);
    };
}

@FunctionalInterface  // 不让子类写其他方法，集成该接口后，子类中只能出现接口中的方法
interface




PayInterface{
    public void payMoney(double money);  // 支付方法
}
