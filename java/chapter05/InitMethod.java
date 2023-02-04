package chapter05;

public class InitMethod {

	int num1, num2;
	public InitMethod(int a, int b) {
		num1 = a;
		num2 = b;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		InitMethod init = new InitMethod(3, 4);
		System.out.println("init.num1="+init.num1+", "+"init.num2="+init.num2);
		
		
	}

}
