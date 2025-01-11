package P1st;

import java.util.Arrays;

public class MaxMinAverage {
    public static void main(String[] args) {
        double[] arr = {8005.95, 7268.01, 10529.00, 7986.50, 9672.66};
        Arrays.sort(arr);
        double res = 0;
        for (double i : arr){
            res += i;
        }
        System.out.printf("最高工资：%.2f，最低工资：%.2f，工资平均值：%.2f", arr[arr.length-1], arr[0], res/arr.length);
    }
}
