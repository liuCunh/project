package chapter06;

class People{
	private String name;
	int age;
	
	public void speak() {
		System.out.println("我会说话");
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void getName() {
		System.out.print(this.name);
	}
}

class Student extends People{
	String id;
	public void study() {
		System.out.println("我的任务是学习");
	}
	
}

class Teacher extends People{
	public void speak() {
		System.out.println("我在教学");
	}
	
}

public class Second {
	public static void main(String[] args) {
		Student stu = new Student();
		Teacher tea = new Teacher();
		stu.setName("刘春");
		stu.age = 20;
		tea.setName("刘春");
		tea.age = 20;
		System.out.print("我叫：");
		stu.getName();
		System.out.print(", 今年："+stu.age+"岁，");
		stu.speak();
		System.out.print("我叫：");
		tea.getName();
		System.out.print(", 今年："+tea.age+"岁，");
		tea.speak();
	}

}
