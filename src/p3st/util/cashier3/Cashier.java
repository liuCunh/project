package p3st.util.cashier3;

public class Cashier {
    private String jobno;  // 工号
    private String name;  // 姓名
    private String department;  // 部门
    private double salary;  // 工资

    public String getJobno() {
        return jobno;
    }

    public void setJobno(String jobno) {
        this.jobno = jobno;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    // 构造方法1
    public Cashier(){}
    // 构造方法2
    public Cashier(String jobno, String name, String department, double salary){
        this.jobno = jobno;
        this.name = name;
        this.department = department;
        this.salary = salary;
    }
    public void introduce(){
        System.out.printf("我叫 %s，在 %s 部门工作，月薪 %.2f\n", name, department, salary);
    }
}
