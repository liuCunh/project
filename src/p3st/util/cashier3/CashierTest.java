package p3st.util.cashier3;

public class CashierTest {
    public static void main(String[] args) {
        // 构造方法1
        Cashier cashier = new Cashier();
        cashier.introduce();
        // 构造方法2
        Cashier cashier1 = new Cashier("10010", "Alex", "IT", 8600.89);
        cashier1.introduce();
    }
}
