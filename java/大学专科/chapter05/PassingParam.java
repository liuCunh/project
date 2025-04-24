package chapter05;

public class PassingParam {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		OneObject obj1 = new OneObject();
		int a = 9;
		System.out.println("Before:a="+a+", obj1.x="+obj1.x);
		changeParam(a, obj1);
		System.out.println("After:a="+a+", obj1.x="+obj1.x);
		
	}
	
	static class OneObject{
		public String x = "a";
	}
	
	static void changeParam(int Y, OneObject obj) {
		Y = 10;
		obj.x = "b";
	}

}
