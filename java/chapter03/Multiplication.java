package JavaPackage;

public class Multiplication {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		long total = 1; // int = 3628800
		for (int i = 1; i <= 10; i++) {
			total *= i;
		}
		System.out.print("1*2*...*10=" + total);
	}

}
