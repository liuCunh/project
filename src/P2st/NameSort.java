package P2st;

import java.util.Scanner;

public class NameSort {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入10为同学姓名(用空格隔开): ");
        scanner.useDelimiter("\n");  // 将scanner的截断符号改为换行
        String ns = scanner.next();
        String[] sn = ns.split(" ");  // 将用户输入转换为数组 bb cc ff dd jj ll aa pp ww kk
        bubbleSort(sn);  // 对名字数组进行排序

        // 对名字输出打印输出
        for (int i = 0; i<sn.length; i++){
            System.out.print(sn[i]+", ");
        }
    }
    // 名字排序方法
    public static void bubbleSort(String[] nums){
        for (int i = 0; i < nums.length; i++){
            for (int j = 0; j < nums.length - i - 1; j++){
                if (nums[j].compareTo(nums[j+1]) > 0){
                    String temp = nums[j];
                    nums [j] = nums[j+1];
                    nums[j+1] = temp;
                }
            }
        }
    }
}
