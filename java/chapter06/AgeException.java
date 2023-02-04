package chapter06;

public class AgeException {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			int age = check("-10");
			System.out.println("age="+age);
		}
		catch(IllegalArgumentException IA) {
			IA.printStackTrace();
			System.out.println("over");
		}
	}	
	
	public static int check(String usAge) throws IllegalArgumentException{
		int age = Integer.valueOf(usAge);
		if(age < 0) {
			throw new IllegalArgumentException();
		}
		return age;
	}
}
