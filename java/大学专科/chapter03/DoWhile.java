package chapter03;

public class DoWhile {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		int a = 1, sum = 0;
//		do {
//			sum += a;
//			a++;
//		}while(a <= 100);
//		
//		System.out.print("1+2+3+..+100="+sum);
		int i = 2, sum = 0;
		do {
			sum += i;
			i += 2;
		}while(i <= 100);
		
		System.out.print("1+2+3+..+100="+sum);
		
	}

}
