package chapter05;

abstract class Fruit {
	String color;
	public abstract void harvest();
}

class Apple extends Fruit {
	String color;
	public Apple(String color) {
		this.color = color;
	}
	
	@Override  // 重载方法的定义
	public void harvest() {
		System.out.println("There is harvest in Apple");
	}
	
}

class FruitExample{
	
	public static void main(String[] args) {
		Apple apple = new Apple("lightblue");
		apple.harvest();
	}
}