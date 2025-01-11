package p3st.util.cashier2;

public class CashierTest {
    public static void main(String[] args) {
        // 实例化收银员对象
        Cashier cashier = new Cashier();
        // 对象赋值
        cashier.setJobno("10010");
        cashier.setName("alex");
        cashier.setDepartment("HR");
        cashier.setSalary(3800.00);
        System.out.printf("jobno: %s, name: %s, department: %s, salary: %.2f", cashier.getJobno(), cashier.getName(), cashier.getDepartment(), cashier.getSalary());
    }
}
