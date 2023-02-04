package chapter06;

public class Except {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a = 6;
		int b = 1;
		try {
			if (b==0)
			throw new ArithmeticException();  // 通过throw语句抛出异常
			System.out.println("a/b="+a/b);
			
		}
		catch(Exception e) {
			System.out.println("error");
		}
		System.out.println("over");
		
		
	}

}
