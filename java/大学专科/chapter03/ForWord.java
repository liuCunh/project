package chapter03;

public class ForWord {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for(int i = 0; i <= 1000; i++) {
			if((i % 7 == 0) && (i % 9 == 0)) {
				System.out.print(i+",");
			}
		}
	}

}
