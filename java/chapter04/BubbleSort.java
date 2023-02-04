package chapter04;

public class BubbleSort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int intArray[] = {12, 25, 88, 9, 63, 6};
		System.out.print("排序前的元素个数：");
		for(int k = 0; k< intArray.length; k++) {
			System.out.print(intArray[k] + " ");
		}
		System.out.println();
		for(int i = intArray.length-1; i > 0; i--) {
			for(int j = 0; j < i; j++) {
				if(intArray[j] < intArray[j+1]) {
					int temp;
					temp = intArray[j];
					intArray[j] = intArray[j+1];
					intArray[j+1] = temp;
				}
			}
			
			System.out.print("地"+i+"次排序结果：");
			for(int k = 0; k< intArray.length; k++) {
				System.out.print(intArray[k] + " ");
			}
			System.out.println();
			
		}
		System.out.print("排序结果：");
		for(int k = 0; k< intArray.length; k++) {
			System.out.print(intArray[k] + " ");
		}
	}

}
