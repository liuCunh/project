package p3st.util.cashier2;

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

    // 获取类的属性
    public void printAttribute(){
        System.out.printf("jobno: %s, name: %s, department: %s", jobno, name, department);
    }

}
