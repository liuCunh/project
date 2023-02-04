package chapter02;

import java.util.Scanner;

public class Triangle {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
//		Scanner edge = new Scanner(System.in);  // 只是引入输入的函数
//		double a = edge.nextDouble();
//		double b = edge.nextDouble();
//		double c = edge.nextDouble();
//		edge.close();
//		
//		double p = (a+b+c) / 2;
//		double area = Math.sqrt(p*(p-a)*(p-b)*(p-c));
//		System.out.println("三角形面积="+area);
//		double perimeter = a+b+c;
//		System.out.println("三角形周长"+perimeter);
		
		
//		boolean judge1 = (a+b) < c;
//		boolean judge2 = (b+c) < a;
//		boolean judge3 = (a+c) < b;
//		boolean res = judge1 || judge2 || judge3;
		
		double a, b, c, perimeter, perimeter1, area;
		Scanner scan = new Scanner(System.in);
		System.out.println("三角形三边:");
		a = scan.nextDouble();
		b = scan.nextDouble();
		c = scan.nextDouble();
		scan.close();
		if ((a+b > c) && (a+c > b) && (b+c > a)) {
		perimeter = a+b+c;
		System.out.println("周长="+perimeter);
		perimeter1 = perimeter / 2;
		area = Math.sqrt(perimeter1 *(perimeter1 - b) * (perimeter1 - a) * (perimeter1 - c));
		System.out.println("面积="+area);
		}else {
			System.out.println("不能构成三角形！");
		}
	}

}
