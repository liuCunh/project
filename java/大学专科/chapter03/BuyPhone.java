package chapter03;

import java.util.Scanner;

public class BuyPhone {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i, user_in;
		double result;
		Scanner sc = new Scanner(System.in);
		result = Double.POSITIVE_INFINITY;  // 正 无穷大
		for(i=0; i < 4; i++) {
			System.out.print("价格：");
			user_in = sc.nextInt();
			
			if(user_in < result) {
				result = user_in;
			}
		}
		sc.close();
		System.out.println(result+"都已经是最低价了，还在等什么！");
	}

}
