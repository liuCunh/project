package chapter05;

public class RoundClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Round round = new Round();
		round.r = 2;
		System.out.println(round.getArea());
		System.out.println(round.getC(4));
	}
	
	static class Round{
		final double PI = 3.14;
		double r;
		
		public double getArea() {
			return PI * r;
		}
		
		public double getC(double d) {
			return PI * d;
		}
	}
	
	
}
