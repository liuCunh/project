package chapter03;

public class While01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i, result;
		i = 2; 
		result = 0;
		while (i <= 100) {
			result += i;
			i += 2;
		}
		System.out.print("result="+result);
		
		int number = 1, sum = 0;
		while (number <= 100) {
			if (number % 2 == 0) {
				sum += number;
			}
			number++;
		}
		System.out.print("2+4+6+...+100="+sum);
	}

}
