package chapter04;
import java.util.*;
public class Exercise {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 多维数组
//		int a[][] = {{1,3},{-5},{3,5,7}};
//		int i,j;
//		System.out.println("length="+a.length);
//		for(i=0; i<a.length;i++) {
//			System.out.println("a[i].length="+a[i].length);
//			for(j=0;j<a[i].length;j++) {
//				System.out.println("a[i][j]="+a[i][j]);
//			}
//		}
		int arrA[][] = {{1,2,3},{4,5,6},{7,8,9},{10,11,12}};
		int arrB[][] = new int[3][4];
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j<4; j++) {
				arrB[i][j] = arrA[j][i];
			}
		}
		int a[] = {2,3,4,5,6};
		int pos = Arrays.binarySearch(a, 0);
		System.out.print(pos);

	}

}
