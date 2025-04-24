package chapter03;

import java.util.Scanner;

public class LifeStage {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.print("Place enter your age:");
		int age = sc.nextInt();
		sc.close();
		
		if (0 <= age && age < 8) {
			System.out.print("child");
		}
		else if(8 <= age && age < 18) {
			System.out.print("teenager");
		}
		else if(18 <= age && age < 60) {
			System.out.print("adult");
		}
		else if(60 <= age && age < 130) {
			System.out.print("retired");
		}
		else {
			System.out.print("enter wrong!");
		}
		
	}

}
