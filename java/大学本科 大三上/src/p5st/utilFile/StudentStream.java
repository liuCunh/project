package p5st.utilFile;

import java.io.*;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class StudentStream {
    public static void main(String[] args) throws IOException {
        Set<Student> studentSet = new HashSet<Student>();
        Student c1 = new Student("2410004", "楚度", "15830422586", 26);
        Student c2 = new Student("2410005", "商心慈", "15825699631", 15);
        studentSet.add(c1);
        studentSet.add(c2);

//        studentSet.forEach(stu -> System.out.println(stu.getMsg()));

        File File = new File("inFileDemo\\customer1.txt");
//        writeData(File, studentSet);
        read(File).forEach(student -> System.out.println(student.getMsg()));
    }
    // 写入
    public static void writeData(File file, Set<Student> studentSet) throws IOException{
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(file));

        // 创建迭代器对象
        Iterator<Student> iterate = studentSet.iterator();
        while(iterate.hasNext()){
            Student student = iterate.next();
            bufferedWriter.write(student.getMsg());
            bufferedWriter.newLine();
            System.out.println(student.getName()+" 添加成功！");
            bufferedWriter.flush();
        }

        bufferedWriter.close();
    }
    // 读取
    public static Set<Student> read(File file) throws IOException{
        BufferedReader bufferedReader = new BufferedReader(new FileReader(file));
        Set<Student> studentSet = new HashSet<Student>();
        String line;
        while((line=bufferedReader.readLine())!=null){
            String[] str = line.split(",");
            Student student = new Student();
            student.setNo(str[0]);
            student.setName(str[1]);
            student.setPhone(str[2]);
            student.setPoints(Integer.parseInt(str[3]));
            studentSet.add(student);
        }
        bufferedReader.close();
        return studentSet;
    }
}

class Student{
    private String no;  // 学号
    private String name;  // 姓名
    private String phone;  // 科目
    private int points;  //成绩
    public Student(){}

    public Student(String no, String name, String phone, int points) {
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

    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }

    public String getMsg(){
        return "%s,%s,%s,%d,".formatted(no, name, phone, points);
    }
}
