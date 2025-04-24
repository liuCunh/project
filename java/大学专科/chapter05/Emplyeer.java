package chapter05;

public class Emplyeer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Person person1 = new Person("Lucy", '女', 23);
		Person person2 = new Person("James", '男', 25);
		person1.walk();
		person2.walk();
		person1.eat();
		person2.eat();
	}
}

class Person{
	String name; int age; boolean gender;
	public Person(String name, char gender, int age) {
		this.name = name;
		this.age = age;
		if(gender == '女') {
			this.gender = false;
		}else {
			this.gender = true;
		}
	}
	
	public void walk() {
		System.out.println(name+"在行走。");
	}
	public void eat() {
		System.out.println(name+"在吃东西。");
	}
}
