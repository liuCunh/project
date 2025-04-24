package exam.util;

public class StudentTest {
    public static void main(String[] args) {
        Student student = new Student("张三", 18);
        student.show();
        Undergraduate undergraduate = new Undergraduate("李四", 21, "本科");
        undergraduate.show();
    }
}

class Student {
    private String name;
    private int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
    public void show(){
        System.out.printf("name: %s, age: %d",name,age);
    }
}
class Undergraduate extends Student{
    private String degree;
    public Undergraduate(String name, int age, String degree) {
        super(name, age);
        this.degree = degree;
    }

    @Override
    public void show() {
        super.show();
        System.out.println(", 学位："+degree);
    }
}
