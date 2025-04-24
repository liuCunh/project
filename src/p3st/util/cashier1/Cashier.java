package p3st.util.cashier1;

public class Cashier {
    String jobno;  // 工号
    String name;  // 姓名

    String department;  // 部门
    double salary;  // 工资

    // 收款行为
    public void proceed(){
        System.out.printf("我是%s，我在收款", name);
    }
}
