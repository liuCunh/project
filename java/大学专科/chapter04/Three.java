package chapter04;

import java.util.Arrays;
import java.util.Scanner;

public class Three {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int usrIn = sc.nextInt();
		sc.close();
		
		int arr[] = {85, 63, 49, 22, 10, 0};
		arr[arr.length-1] = usrIn;
		
		Arrays.sort(arr);
		
		for(int i = 0; i < arr.length; i++) {
			System.out.print(arr[i]+" ");
		}
		
		
	}

}
