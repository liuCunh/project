package p5st.utilFile;

import java.io.*;
import java.util.ArrayList;

public class CharStream {
    public static void main(String[] args) throws IOException {
        String path = "inFileDemo\\customer.txt";  // 文件路径
        ArrayList<Customer> customerArrayList = new ArrayList<Customer>();
        // 创建顾客对象
        Customer c1 = new Customer("2410004", "楚度", "15830422586", 26);
        Customer c2 = new Customer("2410005", "商心慈", "15825699631", 15);
        // 将对象加入集合
        customerArrayList.add(c1);
        customerArrayList.add(c2);

//        writeData(path, customerArrayList);
        customerArrayList.addAll(readData(path));

        customerArrayList.forEach(customer -> System.out.println(customer.getName()));

    }
    // 将集合对象写入文件
    public static void writeData(String path, ArrayList<Customer> customerArrayList) throws IOException{
        // 创建字符缓冲输出流对象
        FileWriter fileWriter = new FileWriter(path);  // 字符流
        BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);  // 缓冲流

        for(int i = 0; i<customerArrayList.size(); i++){
            Customer customer = customerArrayList.get(i);
            StringBuffer stringBuffer = new StringBuffer();
            // 获取顾客对象的数据拼接成为自定格式字符串
            stringBuffer.append(customer.getNo()).append(",").append(customer.getName()).append(",")
                    .append(customer.getPhone()).append(",").append(customer.getPoints()).append(",");
            // 写入文件
            bufferedWriter.write(stringBuffer.toString());
            // 换行
            bufferedWriter.newLine();
            // 强制刷新
            bufferedWriter.flush();
        }
        // 释放资源
        bufferedWriter.close();
    }

    // 文件读取
    public static ArrayList<Customer> readData(String path) throws IOException{
        // 定义顾客集合
        ArrayList<Customer> customerArrayList = new ArrayList<Customer>();
        // 字符缓冲输入流对象
        BufferedReader bufferedReader = new BufferedReader(new FileReader(path));
        String line;
        while ((line= bufferedReader.readLine()) != null){
            String[] str = line.split(", ");  // 按行读取，按照，分割为数组
            Customer customer = new Customer();
            customer.setNo(str[0]);
            customer.setName(str[1]);
            customer.setPhone(str[2]);
            customer.setPoints(Integer.parseInt(str[3].substring(0,2)));
            // 将对象放入集合
            customerArrayList.add(customer);
        }
        bufferedReader.close();
        return customerArrayList;
    }
}

// 顾客类
class Customer{
    private String no;  // 编号
    private String name;  // 姓名
    private String phone;  // 电话
    private Integer points;  // 积分
    public Customer(){}

    public Customer(String no, String name, String phone, Integer points) {
        this.no = no;
        this.name = name;
        this.phone = phone;
        this.points = points;
    }

    public String getNo() {
        return no;
    }

    public void setNo(String no) {
        this.no = no;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public Integer getPoints() {
        return points;
    }

    public void setPoints(Integer points) {
        this.points = points;
    }
}