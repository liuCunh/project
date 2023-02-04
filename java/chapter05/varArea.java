package chapter05;

class variables{
	
	// 成员变量
	static int x=10;  // 类变量
	int y = 20;  // 实例变量
	
	void fun() {
		System.out.println("x="+x);
		System.out.println("y="+y);
		
		// 局部变量
		int x = 100;
		int y = 200;
		System.out.println("x="+x);
		System.out.println("y="+y);
	}
}


public class varArea {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		variables var = new variables();
		var.fun();
	}

}
