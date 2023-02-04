package chapter05;

public class Sort {
	static void BubbleSort(int arr[]) {
		for(int i = arr.length-1; i > 0; i--) {
			for(int j = 0; j < i; j++) {
				if(arr[j] > arr[j+1]) {
					int tmp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = tmp;
				}
			}
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] = new int[10];
		for(int i = 0; i < arr.length; i++) {
			int temp = (int)(Math.random() * 100 + 1);
			arr[i] = temp;
		}
		BubbleSort(arr);
		for(int i = 0; i < arr.length; i++) {
			System.out.print(arr[i]+",");
		}
	}
}
