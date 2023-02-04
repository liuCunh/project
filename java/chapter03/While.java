package chapter03;

public class While {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//初始化
		int a = 1, sum = 0;
		
		//循环体
		while (a <= 100) {
			sum += a;
			a++;
		}
		
		// 输出结果
		System.out.print("1+2+3+4+...+100="+sum);
		

	}

}
