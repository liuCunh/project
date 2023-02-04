package JavaPackage;

public class IsPrime {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for (int i = 2; i < 101; i++) {
			boolean isPrime = true;
			for (int j = 2; j < i; j++) {
//				System.out.println("j="+j);
				if (i % j == 0) {
					isPrime = false;
					break;
				}
			}
//			System.out.println("i="+i+", isPrime="+isPrime);
			if (isPrime) {
				System.out.println(i + "ÊÇËØÊý");
			}
		}
	}

}
